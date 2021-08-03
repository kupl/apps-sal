import re
from statistics import mean
def trump_detector(s): return round(mean(map(len, re.findall(r'(a+|e+|i+|o+|u+)', s.lower()))) - 1, 2)
