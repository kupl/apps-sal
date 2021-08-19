import re


def calculate_string(st):
    st = re.sub('[^-+*/\\d.]', '', st)
    result = eval(st)
    return str(int(round(result)))
