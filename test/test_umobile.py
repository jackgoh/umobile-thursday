from lib import umobile
import json
import pytz
import datetime

phone_number = '0101234567'

# check timezone
tz = pytz.timezone('Asia/Kuala_Lumpur')
date_now = datetime.datetime.now(tz)
today8am = date_now.replace(hour=8, minute=0, second=0, microsecond=0)

def test_get_all_voucher():
    res = umobile.get_voucher_list(phone_number)
    assert res.status_code is 200

def test_get_promo_voucher():
    # get voucher
    res = umobile.get_voucher_list(phone_number)
    voucher_list = json.loads(res.text)

    # get promo voucher
    voucher, campaign_id = umobile.get_promo_voucher(voucher_list)

    if date_now.today().weekday() == 3 and date_now > today8am:
        assert len(campaign_id) == 1
    else:
        assert campaign_id is None



def test_assign_voucher_fail():
    res = umobile.assign_promo_voucher(0, phone_number)
    status = json.loads(res.text)
    print(status['error_message'])
    if date_now.today().weekday() == 3 and date_now > today8am:
        assert status['error_message'] == 'Success'
    else:
        assert status['error_message'] == 'Incomplete parameter'



