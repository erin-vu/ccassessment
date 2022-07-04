# buddy

## This is the First Thing you Should Read

Read this Readme from top to bottom

## Purpose

This project has 3 purposes.

1. Motivation: To give you a feeling for the kind of work you will be doing with us and help you decde if this role is right for you. The best way to know if this work is right for you is if you find this project **fun**. 

<img src="https://www.care.coach/uploads/9/8/5/0/9850803/published/final-care-coach-0970.jpg">

2. Engineering: Although there is no perfect way to assess engineering capabilities generally or specifically, some atttempt is needed, as this role requires both a conceptual and implementation level understanding of machine learning and natural language processing. 

3. Design: You are not supposed to share this code, but inevitably some will violate this agreement. Therefore it is unavoidable that some candidates will have an unfair, early advantage, introduction to the project prior to the interview. However, we are not testing for model performance, and we will be suspicious if the code is too similar to something we have seen before. We are testing for technical communication, which is harder to cheat on and an important part of this project. The intuitiveness of the code, modularity of the functions and classes, absence of unnecessary confusing code, and clear documentation is important. If you end up having a technical interview, your ability to explain to another engineer what you have done, such that they have as much understanding of the code as you do, is the main skill this project is meant to reveal. 

## Setting up a Data Science Environment

Clone this repository (do not fork) and rename it to something else as your own project repository 

I am using python3.8.13 in macOS Monterey Version 12.0.1, but these setup instructions should work as is or with minor edits on most python3 and linux combinations. If you dont have python 3.8 there are many ways to install it, I used [homebrew](https://formulae.brew.sh/formula/python@3.8) and followed the instructions at the end of the download. You have to restart your terminal for the changes to take effect. 

You also need the header files and static libraries for python dev

`sudo apt-get install python3-dev`

1. create a virtual environment for this project and enter that environment. I called mine env_ds but you can call it anything you want. 

```
you@you:/path/to/buddy$ python3.8 -m venv env_ds
you@you:/path/to/buddy$ source env_ds/bin/activate
(env_ds) you@you:/path/to/buddy$ pip install --upgrade pip
```

2. install this project's dependencies from requirements.txt

```
(env_ds) you@you:/path/to/buddy$ pip install -r requirements.txt
```

3. access jupyter notebook from your browser

if you are doing this locally you can just

```
(env_ds) you@you:/path/to/buddy$ jupyter notebook
```

4. your notebook environment should automatically open up as http://localhost:8888/tree where you should click and open up [START_PROJECT.ipynb](START_PROJECT.ipynb) and read the Questions within that notebook to complete this project. 

## How to Submit this Project

email the URL link for your project repository or colab to carson [at] care [dot] coach or whoever your technical interviewer is so they can use it as a reference while you do you technical presentation during the technical interview

The technical interview format is a pretend teaching session where we pretend the interviewer is a student who does not have the same understanding of NLP and transformers that you do now after attempting the project. Your goal is to teach them to understand your code (your repo or colab) and design decisions. As mentioned above, the goal is to evaluate your ability to explain to another engineer what you have done, such that they have as much understanding of the code as you do.

## Frequently Asked Questions

1. how long does this project take? 

One Day. The project is meant to take on average 4 hours total for someone is who is already very familiar with the NLP tools and concepts used here. If you are not already familiar with PyTorch, that is ok. I think if you have a strong python and machine learning background, you can teach yourself most of this within the same free weekend that you use to learn and finish the project. If you have no NLP or ML background, it is hard to estimate how much longer for you this will take. 
