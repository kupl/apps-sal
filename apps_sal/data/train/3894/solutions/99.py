import string


def solve(s):
    if len(s) / len(list(i for i in s if i in string.ascii_lowercase)) <= 2:
        return s.lower()
    else:
        return s.upper()
