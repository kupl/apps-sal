import itertools
def choose_best_sum(t, k, ls):
    n = itertools.combinations(ls,k)
    try: return max([sum(i) for i in n if sum(i) <= t])
    except: return None
