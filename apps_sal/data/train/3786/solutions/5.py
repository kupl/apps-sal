import re
def siegfried(week, s):
    d = {'ph': 'f', 'Ph': 'F','ci': 'si', 'ce': 'se', 'c': 'k', 'Ci': 'Si', 'Ce': 'Se', 'C': 'K','XX':'ch','xx':'Ch','ch':'XX','Ch':'xx','th': 'z', 'wr': 'r', 'wh': 'v', 'w': 'v', 'Th': 'Z', 
        'Wr': 'R', 'Wh': 'V', 'W': 'V','ou': 'u', 'an': 'un', 'ing': 'ink', 'sm': 'schm', 'Ou': 'U', 'An': 'Un', 'Ing': 'Ink', 'Sm': 'Schm'}
    week1=lambda s:re.sub(r'(xx)',lambda x:d[x.group()],re.sub(r'(ci|ce|c)',lambda x:d[x.group()],re.sub(r'(Ch|ch)',lambda x:d[x.group()] ,s),flags=re.I),flags=re.I)
    week2=lambda s:re.sub(r'ph', lambda x: d[x.group()], s, flags=re.I)
    week3=lambda s:re.sub(r'([a-zA-Z])\1', r'\1', re.sub(r'\b([a-zA-Z]+e+)\b',lambda x:x.group()if len(x.group())<=3 else x.group().rstrip('e'),s,flags=re.I), flags=re.I)
    week4=lambda s:re.sub(r'(th|wr|wh|w)', lambda x: d[x.group()], s, flags=re.I)
    week5=lambda s:re.sub(r'(ing(?= )|(?<= )sm)',lambda x:d[x.group()],re.sub(r'(ing$|^sm)',lambda x:d[x.group()],re.sub(r'(ou|an)',lambda x:d[x.group()],s,flags=re.I),flags=re.I),flags=re.I)
    li = [week1, week2, week3, week4, week5]
    for i in li[:week] : s = i(s)
    return s
