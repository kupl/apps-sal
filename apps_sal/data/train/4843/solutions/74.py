from itertools import combinations

def choose_best_sum(t, k, ls):
    ks = list(range(len(ls)))
    
    c = list(combinations(ks, k))
    
    best = 0
    
    for choice in c:
        s = sum(ls[d] for d in choice)
        if not s > t and s > best:
            best = s
    
    return best or None
    
    

