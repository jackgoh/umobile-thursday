import requests
import json

# init
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

def get_voucher_list(phone_number):
    res = session.get(
        "https://mobileapps.u.com.my/prdcampaign/api/top-deals.php?msisdn=6" + str(phone_number) + "&is_u_special=false",
        headers=headers)
    return res

def get_promo_voucher(voucher_list):
    campaign_id = None
    promo_voucher = None
    # loop through all vouchers
    for voucher in voucher_list['vouchers']:
        # find voucher that is thursday promo
        if voucher['is_thursday_promo'] == True and voucher['is_thursday_active'] == True:
            campaign_id = voucher['campaign_id']
            promo_voucher = voucher
    return promo_voucher, campaign_id

def assign_promo_voucher(campaign_id, phone_number):
    res = session.get("https://mobileapps.u.com.my/prdcampaign/api/assign-voucher.php?msisdn=6" + str(
        phone_number) + "&campaign_id=" + str(campaign_id) + "&plan=21", headers=headers)
    redeem_data = json.loads(res.text)
    return res