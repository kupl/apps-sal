def filter_numbers(string):
    return "".join(x for x in string if not (48 <= ord(x) and ord(x) <= 58))
