import re
from math import *


def convert_recipe(s):
    d = {'tsp': 5, 'tbsp': 15}
    matches = re.findall('\\d*/?\\d+ tbsp|\\d*/?\\d+ tsp', s)
    for m in matches:
        (v, k) = m.split()
        x = eval(f'ceil({d.get(k)} * {v})')
        s = s.replace(m, f'{m} ({x}g)', 1)
    return s
