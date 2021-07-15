def indices(n, d):
    from itertools import combinations_with_replacement
    
    lst = []
    for c in combinations_with_replacement(range(n), d):
        base = [0]*n
        for i in c:
            base[i] += 1
        lst.append(base)
    return lst
