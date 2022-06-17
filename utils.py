import sys, random, pickle, os, json, math, re, time

import numpy as np

import torch
import torch.nn.functional as F

class BaseAgent(torch.nn.Module):

    def __init__(self, tokenizer, model):
        
        super().__init__()
        
        self.model = model
        self.tokenizer = tokenizer
        self.optimizer = torch.optim.Adam(
            model.parameters(),
            lr=0.00005,
            betas=(0.9, 0.98),
            eps=1e-9,
        )
        
        self.num_gpus = torch.cuda.device_count()
        
        if self.num_gpus > 1:
            self.model.parallelize()
        else:
            self.model = self.model.cuda()
        
    def get_response(self, prompt, max_len = 32):
        
        prompt_ids = self.tokenizer.encode(
            prompt,
            return_tensors="pt",
        )
        
        if self.num_gpus > 0:
            prompt_ids = prompt_ids.cuda()
        
        prompt_len = prompt_ids.shape[1]
        
        output_ids = self.model.generate(
            prompt_ids,
            max_length=prompt_len+max_len,
        )

        generated_text = self.tokenizer.batch_decode(output_ids)[0]
        
        return generated_text
    
    def memorize(self, prompt, num_epochs = 3):
        
        prompt_dic = self.tokenizer(prompt,return_tensors="pt")
        prompt_ids = prompt_dic.input_ids
        prompt_mask = prompt_dic.attention_mask
        prompt_len = prompt_ids.shape[1]
        
        if self.num_gpus > 0:
            prompt_ids = prompt_ids.cuda()
            
        source_ids = prompt_ids[:,:-1]
        target_ids = prompt_ids[:,1:]
        source_mask = prompt_mask[:,:-1]
        target_mask = prompt_mask[:,1:]

        # allow params to be updated
        self.model.train()

        for e in range(num_epochs):

            # Forward Pass
            output = self.model(
                input_ids = source_ids,
                attention_mask = source_mask,
            )

            # used logits and target tokens to calculate the loss
            logits = output.logits

            scalar_loss = cross_entropy_loss(
                logits, 
                target_ids, 
            )

            # backward pass
            self.optimizer.zero_grad()
            scalar_loss.backward()
            torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1.0)
            self.optimizer.step()

            print("epoch", e, "loss", scalar_loss.item())


def cross_entropy_loss(logits, target_ids):
    
    """
    For F.cross_entropy the Input is shape (N, C), where N = batch_size x sequence_length
    and C is the number of classes, in our case C is the number of tokens in the vocabulary
    Target is shape (N).

    https://pytorch.org/docs/stable/generated/torch.nn.functional.cross_entropy.html

    we flatten the batch dimension together with the max_seq length
    so that for the loss funstion, so afterwards, there is no batch dimension,
    just a vector sized C-dimensions for each of the seq_len tokens. 
    If there had been 2 sampels with a batch size of 2, with 3 tokens in each sample
    then the predictions.shape would be torch.Size([6, 50257])

    Args:
        logits (torch.tensor, float): shape [batch_size, sequence_length, vocab_size]
        target_ids (torch.tensor, int): shape [batch_size, sequence_length]

    Returns: 
        scalar_loss (torch.tensor, scalar float, grad_fn=<NllLossBackward0>)): no shape
            this is a loss you can backpropagate using:

            optimizer.zero_grad()
            scalar_loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()

    """
    
    predictions = logits.view(-1, logits.size(-1))
    target = target_ids.view(-1)

    scalar_loss = F.cross_entropy(
        predictions,
        target,
    )

    return scalar_loss