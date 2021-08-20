import re


def remove_chars(s):
    return re.sub('[^a-z A-Z]', '', s)
