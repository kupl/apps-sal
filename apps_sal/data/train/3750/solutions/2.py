import re


def count_letters_and_digits(s):
    if s == None or s == []:
        return 0
    return len(re.findall("[A-Za-z0-9]", s))
