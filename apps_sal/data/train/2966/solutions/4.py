import re
def calculate(string):
    return eval(re.sub("[^\d+-]", "", string.replace("loses", "-").replace("gains", "+")) )
