import re


def solve(s):
    zahlen = re.findall('([0-9]*)', s)
    liste = [feld for feld in zahlen if feld != '']
    results = list(map(int, liste))
    return max(results)
