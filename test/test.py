from lib import umobile

phone_number = 0101234567

def test_get_all_voucher():
    res = umobile.get_voucher_list(phone_number)
    assert res.status_code is 200

''''
def test_get_promo_voucher():
    res = umobile.get_promo_voucher()
    assert res.status_code is 200

def test_assign_voucher_success():
    res = umobile.assign_promo_voucher()
    assert res.status_code is 200

def test_assign_voucher_fail():
    assert res.status_code is 200
'''