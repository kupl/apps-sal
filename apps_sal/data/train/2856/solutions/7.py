import re

def gap(num):
    num = bin(num)[2:]
    return max(map(len, re.findall("(?<=1)0+(?=1)", num)), default=0)
