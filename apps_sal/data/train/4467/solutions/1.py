from collections import Counter

def remember(str_):
    seen, lst = Counter(), []
    for c in str_:
        if seen[c] == 1: lst.append(c)
        seen[c] += 1
    return lst
