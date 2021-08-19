import re


def calculate(s):
    try:
        return eval(re.sub('\\b0+(?=[1-9])', '', s))
    except:
        return False
