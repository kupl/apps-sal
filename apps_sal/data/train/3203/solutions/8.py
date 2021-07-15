from itertools import groupby
import re
def parse_mana_cost(mana):
    result = {}
    pattern = re.compile(r'\d*[wurbg]*', re.I)
    manacost = pattern.match(mana).group()
    if mana in ['', '0']:
        return {}
    if manacost == None or len(mana) != len(manacost):
        return None
    colors, colorless = '', ''
    for i in manacost:
        if i.isalpha():
            colors += i
        else:
            colorless +=i
    if colorless not in ['0', '']:
        result['*'] = int(colorless)
    colors = ''.join(sorted(list(colors)))
    for key, count in groupby(colors):
        result[key.lower()] = len(list(count))
    return result

