import string as str


def to_alternating_case(string):
    res = ''
    for i in string:
        if i in str.ascii_lowercase:
            res += i.upper()
        elif i in str.ascii_uppercase:
            res += i.lower()
        else:
            res += i
    return res
