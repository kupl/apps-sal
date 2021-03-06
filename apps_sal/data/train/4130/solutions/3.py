from re import match, search


def is_valid_HK_phone_number(number):
    return bool(match('\\d{4}\\s\\d{4}\\Z', number))


def has_valid_HK_phone_number(number):
    return bool(search('\\d{4}\\s\\d{4}', number))
