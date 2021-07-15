import re
def is_valid_HK_phone_number(number):
    return len(number) == 9 and has_valid_HK_phone_number(number)
    
def has_valid_HK_phone_number(number):
    return bool(re.search(r'\d{4}\s\d{4}', number))
