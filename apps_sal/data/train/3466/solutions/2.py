check = __import__('re').compile('\\d\\d-\\d\\d-\\d\\d\\d\\d \\d\\d:\\d\\d').fullmatch


def date_checker(date):
    return bool(check(date))
