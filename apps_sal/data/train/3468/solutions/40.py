from collections import Counter
def scramble(s1, s2):
    a = Counter(s1)
    b = Counter(s2)

    
    for k,v in b.items():
        if k not in a.keys() or a[k] < v:
            return False
    
    return True
