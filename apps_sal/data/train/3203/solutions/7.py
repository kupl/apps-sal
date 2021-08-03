import re


def parse_mana_cost(mana):
    mana = mana.lower()
    valid = ['w', 'u', 'r', 'g', 'b']
    dic = {}
    regex = re.compile(r'(\d*)([wubrg]*)')
    match = regex.search(mana)

    for x in list(mana):
        if x in valid:
            dic[x] = dic[x] + 1 if x in dic else 1

    if match.group(1) and match.group(1) != '0':
        dic['*'] = int(match.group(1))

    return dic if ''.join(match.group()) == mana else None
