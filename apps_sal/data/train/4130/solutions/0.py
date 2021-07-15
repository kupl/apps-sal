import re

HK_PHONE_NUMBER = '\d{4} \d{4}'

def is_valid_HK_phone_number(number):
    return bool(re.match(HK_PHONE_NUMBER+'\Z',number))

def has_valid_HK_phone_number(number):
    return bool(re.search(HK_PHONE_NUMBER,number))
