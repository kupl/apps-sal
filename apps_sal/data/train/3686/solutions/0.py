import re


def calculate(input):
    try:
        return eval(re.sub(r'(\d+)', lambda m: str(int(m.group(1))), input))
    except:
        return False
