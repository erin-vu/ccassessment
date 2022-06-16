# buddy

## This is the First Thing you Should Read

This project has 3 purposes.

1. To give you a feeling for the kind of work you will be doing with us and help you decde if this role is right for you. The best way to know is if you find this project **fun**

## Setting up a Data Science Environment

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