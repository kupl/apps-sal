CRITERIA = (str.islower, str.isupper, str.isdigit)


def password(s):
    return len(s) > 7 and all(any(map(f, s)) for f in CRITERIA)
