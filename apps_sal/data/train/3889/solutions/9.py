import re


def area_code(text):
    return re.search('\\((.*)\\)', text).group(1)
