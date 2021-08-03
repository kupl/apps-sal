import re


def siegfried(week, s):
    d = {'ph': 'f', 'Ph': 'F', 'ci': 'si', 'ce': 'se', 'c': 'k', 'Ci': 'Si', 'Ce': 'Se', 'C': 'K', 'XX': 'ch', 'xx': 'Ch', 'ch': 'XX', 'Ch': 'xx', 'th': 'z', 'wr': 'r', 'wh': 'v', 'w': 'v', 'Th': 'Z',
         'Wr': 'R', 'Wh': 'V', 'W': 'V', 'ou': 'u', 'an': 'un', 'ing': 'ink', 'sm': 'schm', 'Ou': 'U', 'An': 'Un', 'Ing': 'Ink', 'Sm': 'Schm'}

    def week1(s): return re.sub(r'(xx)', lambda x: d[x.group()], re.sub(r'(ci|ce|c)', lambda x: d[x.group()], re.sub(r'(Ch|ch)', lambda x: d[x.group()], s), flags=re.I), flags=re.I)
    def week2(s): return re.sub(r'ph', lambda x: d[x.group()], s, flags=re.I)
    def week3(s): return re.sub(r'([a-zA-Z])\1', r'\1', re.sub(r'\b([a-zA-Z]+e+)\b', lambda x: x.group()if len(x.group()) <= 3 else x.group().rstrip('e'), s, flags=re.I), flags=re.I)
    def week4(s): return re.sub(r'(th|wr|wh|w)', lambda x: d[x.group()], s, flags=re.I)
    def week5(s): return re.sub(r'(ing(?= )|(?<= )sm)', lambda x: d[x.group()], re.sub(r'(ing$|^sm)', lambda x: d[x.group()], re.sub(r'(ou|an)', lambda x: d[x.group()], s, flags=re.I), flags=re.I), flags=re.I)
    li = [week1, week2, week3, week4, week5]
    for i in li[:week]:
        s = i(s)
    return s
