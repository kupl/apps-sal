def date_checker(s):
    return bool(__import__('re').match('\\d\\d-\\d\\d-\\d{4} \\d\\d:\\d\\d', s))
