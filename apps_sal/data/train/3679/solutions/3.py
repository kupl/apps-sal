import re


def calculate_string(st):
    return str(round(eval(re.sub('[^0-9\\-\\+\\*\\/\\.]', '', st))))
