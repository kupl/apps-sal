import re

PATTERNS = [re.compile(r'(?i)ci|ce|c(?!h)'),
            re.compile(r'(?i)ph'),
            re.compile(r'(?i)(?<!\b[a-z]{1})(?<!\b[a-z]{2})e\b|([a-z])\1'),
            re.compile(r'(?i)th|w[rh]?'),
            re.compile(r'(?i)ou|an|ing\b|\bsm')]
            
CHANGES  = {"ci": "si", "ce": "se", "c":"k",                     # Week 1
            "ph": "f",                                           # Week 2
            "th": "z",  "wr": "r",  "wh":  "v",   "w": "v",      # Week 4
            "ou": "u",  "an": "un", "ing": "ink", "sm": "schm"}  # Week 5

def change(m):
    tok = m.group(0)
    rep = CHANGES.get( tok.lower(), "" if None in m.groups() else m.group()[0] )        # default value used for week 3 only
    if tok[0].isupper(): rep = rep.title()
    return rep
        
def siegfried(week, txt):
    for n in range(week):
        txt = PATTERNS[n].sub(change, txt)
    return txt
