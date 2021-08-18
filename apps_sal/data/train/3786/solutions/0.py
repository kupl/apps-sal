import re

PATTERNS = [re.compile(r'(?i)ci|ce|c(?!h)'),
            re.compile(r'(?i)ph'),
            re.compile(r'(?i)(?<!\b[a-z]{1})(?<!\b[a-z]{2})e\b|([a-z])\1'),
            re.compile(r'(?i)th|w[rh]?'),
            re.compile(r'(?i)ou|an|ing\b|\bsm')]

CHANGES = {"ci": "si", "ce": "se", "c": "k",
           "ph": "f",
           "th": "z", "wr": "r", "wh": "v", "w": "v",
           "ou": "u", "an": "un", "ing": "ink", "sm": "schm"}


def change(m):
    tok = m.group(0)
    rep = CHANGES.get(tok.lower(), "" if None in m.groups() else m.group()[0])
    if tok[0].isupper():
        rep = rep.title()
    return rep


def siegfried(week, txt):
    for n in range(week):
        txt = PATTERNS[n].sub(change, txt)
    return txt
