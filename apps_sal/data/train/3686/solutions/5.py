import re

def calculate(input):
    try:
        for n in re.findall("\d+", input):
            input = input.replace(n, (n.lstrip("0") or "0"))
        return eval(input)
    except: return False
