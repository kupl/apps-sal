import re


def siegfried(week, txt):
    w = []
    t = txt.replace('ci', 'si').replace('Ci', 'Si').replace('ce', 'se').replace('Ce', 'Se').replace('c', 'k').replace('C', 'K').replace('kh', 'ch').replace('Kh', 'Ch')
    w.append(t)
    t = t.replace('ph', 'f').replace('Ph', 'F')
    w.append(t)
    t = re.sub(r'([A-Za-z])\1', r'\1', re.sub(r'([a-zA-Z]{3,})e\b', r'\1', t), flags=re.I)
    w.append(t)
    t = t.replace('th', 'z').replace('Th', 'Z').replace('wr', 'r').replace('Wr', 'R').replace('wh', 'v').replace('Wh', 'V').replace('w', 'v').replace('W', 'V')
    w.append(t)
    t = re.sub(r'\b(s|S)(m)', r'\1ch\2', re.sub(r'ing\b', r'ink', t.replace('ou', 'u').replace('an', 'un').replace('An', 'Un')))
    w.append(t)
    return w[week - 1]
