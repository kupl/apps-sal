from collections import Counter

def count_sel(lst):
    c = Counter(lst)
    length = len(lst)
    unique = len(c)
    once = sum(1 for elem, cnt in c.items() if cnt == 1)
    max_occur = max(c.values())
    most = sorted(elem for elem, cnt in c.items() if cnt == max_occur)
    
    return [length, unique, once, [most, max_occur]]
