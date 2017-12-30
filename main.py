import time
import requests 
import sys
import json
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from optparse import OptionParser

# init
campaign_id = None
promo_voucher = None
redeem_state = True
headers={"Host": "mobileapps.u.com.my",
"Accept-Encoding": "br, gzip, deflate",
"Connection": "keep-alive",
"Accept": "*/*",
"User-Agent": "MyUMobile/1264 CFNetwork/889.9 Darwin/17.2.0",
"Authorization": "Basic XXXXXXXXXXXXXXXXXXXXXXXX",
"Accept-Language": "en-sg",
"X-Umobile-Client-Build": "iOS_1264"}

session = requests.session()

# parser 
parser = OptionParser()
parser.add_option("-n", "--number", dest="phone_number",
                  help="Your Umobile Phone Number without +6")
(options, args) = parser.parse_args()

if not options.phone_number:
    print('Error: Run with -n. Eg: python main.py -n 0181234567')
    sys.exit()

phone_num = options.phone_number

while redeem_state:
    try:
        # get vouchers 
        res = session.get("https://mobileapps.u.com.my/prdcampaign/api/top-deals.php?msisdn=6"+ str(phone_num) +"&is_u_special=false", headers=headers)
        data = json.loads(res.text)

        # loop through all vouchers 
        for voucher in data['vouchers']:
            # find voucher that is thursday promo 
            if voucher['is_thursday_promo'] == True and voucher['is_thursday_active'] == True:
                campaign_id = voucher['campaign_id']
                promo_voucher = voucher 
            
        campaign_id = 820
        # check if promo voucher exist 
        if campaign_id == '0' or not campaign_id:
            print('not yet')
        else:
            # redeem vouchers
            res = session.get("https://mobileapps.u.com.my/prdcampaign/api/assign-voucher.php?msisdn=6"+ str(phone_num) +"&campaign_id="+ str(campaign_id) +"&plan=21", headers=headers)
            redeem_data = json.loads(res.text)

            if res.status_code == 200:
                print('sucess', promo_voucher)
            else:
                print('failed', redeem_data)

            redeem_state = False

    except Exception as e:
        time.sleep(2)
        print(e)