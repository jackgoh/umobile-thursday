import time
import requests 
import sys
from optparse import OptionParser
from lib import umobile

state = True
session = requests.session()

# parser 
parser = OptionParser()
parser.add_option("-n", "--number", dest="phone_number",
                  help="Your Umobile Phone Number without +6")
(options, args) = parser.parse_args()

if not options.phone_number:
    print('Error: Run with -n. Eg: python main.py -n 0181234567')
    sys.exit()

phone_number = options.phone_number

while state:
    try:
        voucher = umobile.get_voucher_list(phone_number)
        voucher_list = json.loads(voucher.text)
        promo_voucher, campaign_id = umobile.get_promo_voucher(voucher_list)
        return_data = umobile.assign_promo_voucher(campaign_id, phone_number)
        if return_data.status_code == 200:
            print('success')
        else:
            print('failed', return_data.text)
        state = False

    except Exception as e:
        print(e)
