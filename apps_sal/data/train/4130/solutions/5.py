import re

VALID_PHONE = re.compile(r'\d{4} \d{4}')

def is_valid_HK_phone_number(number):
    return len(number)==9 and bool(VALID_PHONE.match(number))

def has_valid_HK_phone_number(number):
    return bool(VALID_PHONE.search(number))
