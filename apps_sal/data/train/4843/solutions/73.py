def choose_best_sum(t, k, ls):
    print((t,k, ls))
    ls = [a for a in sorted(ls) if a <= t]
    if len(ls) < k:
        return None
    return _choose_best_sum(t, k, ls)
    
def _choose_best_sum(t, k, ls):    
    if k == 1:
        w = [a for a in ls if a <= t]
        if w:
            return w[-1]
        else: 
            return None
    if sum(ls[:k]) > t:
        return None
    las_sum = sum(ls[-k:])
    if las_sum < t:
        return las_sum
    
    r = None
    for i in range(1, len(ls) - k + 2):        
        val = ls[-i]
        if val > t:
            continue  
        
        l = ls[:]
        del l[-i]
        result = _choose_best_sum(t-val, k-1, l)
        if result is not None:
            if r is not None:
                r = max(r, result + val)
            else:
                r = result + val
    if r is not None:
        return r
    return None
