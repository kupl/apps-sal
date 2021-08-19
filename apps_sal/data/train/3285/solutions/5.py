import re
from statistics import mean


def trump_detector(s):
    return round(mean(map(len, re.findall('(a+|e+|i+|o+|u+)', s.lower()))) - 1, 2)
