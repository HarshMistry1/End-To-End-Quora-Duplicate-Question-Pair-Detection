
# Quora Duplicate Question Pair Detection

Built an End to end web application to find out whether the given quora questions are duplicated or not.

## Table Of Contents

* [Overview](#overview)
* [Motivation](#motivation)
* [Problem Statement](#problem-statement)
* [Web App Link](#web-app-link)
* [Installation](#installation)
* [Technincal Aspect](#technical-aspect)
* [Tech Stack](#tech-stack)
* [Bug Report](#bug-report)
* [Shout Out](#shout-out)
* [Reach Me Out](#reach-me-out)

## Overview
Quora is a place to gain and share knowledge—about anything. It’s a platform to ask questions and connect with people who contribute unique insights and quality answers. This empowers people to learn from each other and to better understand the world.
## Motivation

*"The motivation was to experiment with end to end machine learning project and get some idea about deployment platform like [AWS Services](https://aws.amazon.com/) and of course [Heroku](https://g.co/kgs/yvsR77)."*

Over 100 million people visit Quora every month, so it's no surprise that many people ask similarly worded questions. Multiple questions with the same intent can cause seekers to spend more time finding the best answer to their question, and make writers feel they need to answer multiple versions of the same question. Quora values canonical questions because they provide a better experience to active seekers and writers, and offer more value to both of these groups in the long term.

## Problem Statement

Identify which questions asked on Quora are duplicates of questions that have already been asked. This could be useful to instantly provide answers to questions that have already been answered. We are tasked with predicting whether a pair of questions are duplicates or not.

## Web App Link

[Visit the link](https://ec2-3-75-235-60.eu-central-1.compute.amazonaws.com:8501)

## Installation
- 1 : Open up a directory and create a virtual environment `python -m venv 'name-of-vir-env'`
- 2 : Activate the environment by `.\'name-of-vir-env'\Scripts\activate'`.
- 3 : Now, install the packages `pip install -r requirements.txt`.

## Technical Aspect

- Training a machine learning model using Bag of words technique. 
- Building and hosting a Streamlit web app on AWS EC2 Instance on Ubuntu AMI Machine. 
- A user has to enter the questions on their Input. 
- Once it get all the questions, the prediction is displayed on same page.

## Tech Stack

<img target="_blank" src="https://github.com/HarshMistry1/End-To-End-Quora-Duplicate-Question-Pair-Detection/blob/master/logos/Pandas_logo.png" width=170>
<img target="_blank" src="https://github.com/HarshMistry1/End-To-End-Quora-Duplicate-Question-Pair-Detection/blob/master/logos/Plotly-logo.png" width=170>
<img target="_blank" src="https://github.com/HarshMistry1/End-To-End-Quora-Duplicate-Question-Pair-Detection/blob/master/logos/streamlit-logo.png" width=170>


## Bug Report
If you find a bug (or any result which should need to be improved), kindly open an issue [here](https://github.com/HarshMistry1/End-To-End-Quora-Duplicate-Question-Pair-Detection/issues), by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/HarshMistry1/End-To-End-Quora-Duplicate-Question-Pair-Detection/issues/new). Please include sample queries and their corresponding results.

## Shout Out
* [Nitish Singh](https://www.youtube.com/@campusx-official) - For Idea, Real world problem and Deployment.
* [Uday Paila (Udi Bhaskar)](https://github.com/UdiBhaskar) - For Business Perspective and Out of the box vision.


## Reach Me Out
If you have any feedback, please reach out to me at Harshsutharinfo@gmail.com.
