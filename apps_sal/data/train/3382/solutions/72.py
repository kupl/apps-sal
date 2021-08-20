import string


def lowercase_count(s):
    return sum((1 for x in s if x in string.ascii_lowercase))
