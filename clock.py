from apscheduler.schedulers.blocking import BlockingScheduler
import time
import requests 
import os
from lib import umobile
import json
import sys
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

session = requests.session()
sched = BlockingScheduler({'apscheduler.timezone': 'Asia/Kuala_Lumpur'})

# check if phone exist
if not os.environ['PHONE_NUM']:
    print('Phone number not found in ENV')
    sys.exit()

@sched.scheduled_job('cron', day_of_week='thu', hour=8, minute=0)
def main():
    phone_number = os.environ['PHONE_NUM']
    state = True
    while state:
        try:
            voucher = umobile.get_voucher_list(phone_number)
            voucher_list = json.loads(voucher.text)

            promo_voucher, campaign_id = umobile.get_promo_voucher(voucher_list)

            if campaign_id == '0' or not campaign_id:
                time.sleep(5)
                print('No promo voucher yet, retrying in 5 seconds')
            else:
                return_data = umobile.assign_promo_voucher(campaign_id, phone_number)
                if return_data.status_code == 200:
                    print('Success! you grabbed', promo_voucher['title'])
                else:
                    print('failed', return_data.text)
                state = False

        except Exception as e:
            print('Server error, retrying in 3 seconds..', e)
            time.sleep(3)

sched.start()