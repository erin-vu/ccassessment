# buddy

## This is the First Thing you Should Read

Read this Readme from top to bottom

## Purpose

This project has 3 purposes.

1. Motivation: To give you a feeling for the kind of work you will be doing with us and help you decde if this role is right for you. The best way to know if this work is right for you is if you find this project **fun**. 

<img src="https://www.care.coach/uploads/9/8/5/0/9850803/published/final-care-coach-0970.jpg">

2. Engineering: Although there is no perfect way to assess engineering capabilities generally or specifically, some atttempt is needed, as this role requires both a conceptual and implementation level understanding of machine learning and natural language processing. 

3. Design: Sharing of code is inevitable, therefore it is unavoidable that some candidates will have an unfair, early advantage, introduction to the project prior to the interview. However, technical communication is harder to cheat on and an important part of this demonstration. The intuitiveness of the code, modularity of the functions and classes, absence of unnecessary confusing code, clear documentation and the ability to explain to another engineer such that they have as much control and understanding of the codebase as the original creator, are probably the most important skills this project is meant to reveal. 

## Setting up a Data Science Environment

Fork this repository to your own GitHub and keep the most updated version there.

I am using python3.8.13 in macOS Montery Version 12.0.1, but these setup instructions should work as is or with minor edits on most python3 and linux combinations. If you dont have python 3.8 there are many ways to install it, I used [homebrew](https://formulae.brew.sh/formula/python@3.8) and followed the instructions at the end of the download. You have to restart your terminal for the changes to take effect. 

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

email the GitHub URL link for your forked project to carson [at] care [dot] coach 

## Frequently Asked Questions

1. how long does this project take? 

The project is meant to take about 4 hours total for someone is who is already very familiar with the NLP tools and concepts used here. If you are not already familiar with PyTorch, that is ok. I think if you have a strong python, data science and machine learning background, you can teach yourself most of this within the same free weekend that you use to learn and finish the project, or be able to finish this within the week working on it an hour each night of the week. If you have no NLP or ML background, it is hard to estimate how much longer for you this will take. 