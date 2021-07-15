from collections import defaultdict
from itertools import chain
import re

p1 = re.compile("(.*?)\s*(\d+)")
p2 = re.compile("-| ")

def change(s):
    L = p2.split(s)
    if len(L) == 1:
        return L[0][:6].upper()
    if len(L) == 2:
        return (L[0][:3] + L[1][:3]).upper()
    if len(L) == 3:
        return (L[0][:2] + L[1][:2] + L[2][:2]).upper()
    if len(L) == 4:
        return (L[0][0] + L[1][0] + L[2][:2] + L[3][:2]).upper()
    raise Exception("No rule for more than 4 words")

def create_report(names):
    result = defaultdict(int)
    for data in names:
        name, num = p1.match(data).groups()
        if name == "Labrador Duck": return ["Disqualified data"]
        result[change(name)] += int(num)
    return list(chain.from_iterable(sorted(result.items())))
