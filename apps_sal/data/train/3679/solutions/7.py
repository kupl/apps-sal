import re

def calculate_string(st):
    s = re.sub( '[^0-9+-/*]+', '', st)
    s = s.replace(',', '')
    return str(round(eval(s)))
