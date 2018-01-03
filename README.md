# UMobile TERER Thursday Grabber
[![Maintainability](https://api.codeclimate.com/v1/badges/d54491e0402f4e021a0b/maintainability)](https://codeclimate.com/github/jackgoh/umobile-thursday/maintainability)
[![Build Status](https://travis-ci.org/jackgoh/umobile-thursday.svg?branch=master)](https://travis-ci.org/jackgoh/umobile-thursday)

Automatically grab UMobile TERER Thursday deal without interacting with mobile apps. 

##### Currently still under development. Require running it manually every Thursday or Wednesday night.

## Usage
- Clone this repo `git clone git@github.com:jackgoh/umobile-thursday.git` 
- Install dependencies `pip install -r requirements.txt`
- Run main.py -n [phone number] `python main.py -n 0181234567`

## Cronjob 
Use crontab to add job 
 `crontab -e` 

Add following line to crontab `0 8 * * 4 nohup python /paath_to_project/main.py > /tmp/umobile_grabber.log 2>&1`

Note: More info about crontab refers to http://corntab.com
## Todo
- [x] List and assign voucher to account
- [x] Error handling
- [x] Complete test 
- [x] Integrate Travis
- [x] Cronbjob guide
- [ ] Web Service 