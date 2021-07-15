from itertools import combinations

def choose_best_sum(t, k, ls):
    best = (-1, None) # (best total distance travelled, the combination that gives you that)
    for i in combinations(ls, k):
        if (sum(i) <= t) and (sum(i) > best[0]):
            best = (sum(i), i)
    print(best)
    if best[0] == -1:
        return(None)
    return(best[0])
