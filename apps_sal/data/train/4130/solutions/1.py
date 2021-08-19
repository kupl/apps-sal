from re import match, search


def is_valid_HK_phone_number(n):
    return match('^\\d{4} \\d{4}$', n) is not None


def has_valid_HK_phone_number(n):
    return search('\\d{4} \\d{4}', n) is not None
