import itertools
def choose_best_sum(t, k, ls):
    ls = [val for val in ls if (k > 1) and (val < t) or (val<=t)]
    ls.sort()
    if len(ls) < k: return None
    minsum = sum(ls[:k])
    if minsum > t: return None
    if minsum == t: return t
    max = 0
    for l in itertools.combinations(ls, k):
        s = sum(l)
        if s > t: continue
        if s == t: return t
        if s > max: max = s
    return max

