import re


def count_letters_and_digits(s):
    s = re.sub('[^\\w]', '', s)
    s = s.replace('_', '')
    return len(s)
