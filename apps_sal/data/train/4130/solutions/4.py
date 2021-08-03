import re


def is_valid_HK_phone_number(number):
    return bool(re.search(r'^\d{4} \d{4}$', number))


def has_valid_HK_phone_number(number):
    return bool(re.search(r'\d{4} \d{4}', number))
