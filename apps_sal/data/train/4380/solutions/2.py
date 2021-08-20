import re


def remove_chars(s):
    return re.sub('[^A-Za-z\\s]', '', s)
