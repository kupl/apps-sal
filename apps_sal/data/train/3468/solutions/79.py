from collections import Counter

def scramble(s1, s2):
    d1 = dict(Counter(s1))
    d2 = dict(Counter(s2))
    d3 = {k: v for k,v in d1.items() if k in d2.keys()}
    missing = {k:v for k,v in d2.items() if k not in d3}
    
    if len(missing) >= 1:
        return False
    elif len(s2) == 0 or len(s1) == 0:
        return False
    elif len(missing) == 0:
        calc = {k: d3[k]- d2[k] for k in d2.keys() & d3}
        return True if all(value >= 0 for value in calc.values()) else False
