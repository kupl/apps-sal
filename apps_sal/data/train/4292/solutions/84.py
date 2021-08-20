import re


def string_clean(s):
    delNum = re.compile('[^0123456789]')
    return ''.join(delNum.findall(s))
