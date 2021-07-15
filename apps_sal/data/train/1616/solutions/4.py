import re

SIMPLIFIER = re.compile(r'(\s|-|\band)+')
SPLITTER   = [re.compile(rf'\s*{what}\s*') for what in ('million', 'thousand', 'hundred', r'ty\b')]
COEFS      = [10**x for x in (6,3,2,1)]

vals       = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
VALUES     = {name:v for name,v in zip(vals, range(len(vals)))}
VALUES.update({'twen': 2, 'thir': 3, 'for': 4, 'fif': 5, 'eigh':8})


def parse_int(s): 
    return parse(0, SIMPLIFIER.sub(' ',s.lower()))

def parse(i, s):
    if i == len(SPLITTER): return VALUES.get(s,0)
        
    lst, coef, i = SPLITTER[i].split(s), COEFS[i], i+1
    
    return parse(i,lst[0]) if len(lst)==1 else coef * parse(i,lst[0]) + parse(i,lst[1])
