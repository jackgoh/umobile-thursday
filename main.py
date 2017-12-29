import time
import requests 
import sys
import json

state = False
campaign_id = None
headers={"Host": "mobileapps.u.com.my",
"Accept-Encoding": "br, gzip, deflate",
"Connection": "keep-alive",
"Accept": "*/*",
"User-Agent": "MyUMobile/1264 CFNetwork/889.9 Darwin/17.2.0",
"Authorization": "Basic XXXXXXXXXXXXXXXXXXXXXXXX",
"Accept-Language": "en-sg",
"X-Umobile-Client-Build": "iOS_1264"}

def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    #session.proxies = {'http':  'socks5://127.0.0.1:9150',
    #                   'https': 'socks5://127.0.0.1:9150'}
    return session

while not state:
    # get vouchers 
    session = get_tor_session()
    res = session.get("https://mobileapps.u.com.my/prdcampaign/api/top-deals.php?msisdn=asd&is_u_special=false", headers=headers)
    data = json.loads(res.text)

    for vouchers in data['vouchers']:
        if vouchers['is_thursday_promo'] == True and vouchers['is_thursday_active'] == True:
            campaign_id = vouchers['campaign_id']
            print(vouchers)

        if campaign_id:
            if campaign_id == '0':
                print('not yet')
            else:
                # redeem vouchers
                res = session.get("https://mobileapps.u.com.my/prdcampaign/api/assign-voucher.php?msisdn=asd&campaign_id="+ str(campaign_id) +"&plan=21", headers=headers)
                redeem_data = json.loads(res.text)

                if res.status_code == 200:
                    print('sucess')
                    state = True
                else:
                    print('failed', redeem_data)