def uni_total(string):
    if not string:
        return 0
    return sum([ord(s) for s in string])
