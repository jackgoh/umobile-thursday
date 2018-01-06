# UMobile TERER Thursday Grabber
[![Maintainability](https://api.codeclimate.com/v1/badges/d54491e0402f4e021a0b/maintainability)](https://codeclimate.com/github/jackgoh/umobile-thursday/maintainability)
[![Build Status](https://travis-ci.org/jackgoh/umobile-thursday.svg?branch=master)](https://travis-ci.org/jackgoh/umobile-thursday)

Automatically grab UMobile TERER Thursday deal without interacting with mobile apps. 

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## View logs
- Install Heroku CLI https://devcenter.heroku.com/articles/heroku-cli
- `heroku logs` 

## Running locally 
### Installation
- Clone this repo `git clone git@github.com:jackgoh/umobile-thursday.git` 
- Install Python 3.5 
- Install dependencies `pip install -r requirements.txt`

### Usage 
- create `.env` file in root folder
- add `PHONE_NUM=0100000000` to `.env` file
- run `python clock.py`