import re


def calculate(s):
    try:
        s = re.sub('(?<!\\d)0+(0|[1-9]\\d*)', lambda m: m.group(1), s)
        s = re.sub('\\d+(?!\\.)', lambda m: m.group() + '.0', s)
        return eval(s)
    except:
        return False
