# Really, nothing to check if days and motnhs and zeroes or too high?
check = __import__("re").compile(r"\d\d-\d\d-\d\d\d\d \d\d:\d\d").fullmatch

def date_checker(date):
    return bool(check(date))
