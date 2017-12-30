import time
import requests 
import sys
import json
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

state = False
campaign_id = None
promo_voucher = None
headers={"Host": "mobileapps.u.com.my",
"Accept-Encoding": "br, gzip, deflate",
"Connection": "keep-alive",
"Accept": "*/*",
"User-Agent": "MyUMobile/1264 CFNetwork/889.9 Darwin/17.2.0",
"Authorization": "Basic XXXXXXXXXXXXXXXXXXXXXXXX",
"Accept-Language": "en-sg",
"X-Umobile-Client-Build": "iOS_1264"}

session = requests.session()

while True:
    try:
        # get vouchers 
        res = session.get("https://mobileapps.u.com.my/prdcampaign/api/top-deals.php?msisdn=60180000000&is_u_special=false", headers=headers)
        data = json.loads(res.text)

        # loop through all vouchers 
        for voucher in data['vouchers']:

            # find voucher that is thursday promo 
            if vouchers['is_thursday_promo'] == True and vouchers['is_thursday_active'] == True:
                campaign_id = voucher['campaign_id']
                promo_voucher = voucher 
            
            # check if promo voucher exist 
            if campaign_id == '0' or not campaign_id:
                print('not yet')
            else:
                # redeem vouchers
                res = session.get("https://mobileapps.u.com.my/prdcampaign/api/assign-voucher.php?msisdn=asd&campaign_id="+ str(campaign_id) +"&plan=21", headers=headers)
                redeem_data = json.loads(res.text)

                if res.status_code == 200:
                    print('sucess', promo_voucher)
                    break
                else:
                    print('failed', redeem_data)

    except:
        time.sleep(1)
        print('request error, probably timeout')