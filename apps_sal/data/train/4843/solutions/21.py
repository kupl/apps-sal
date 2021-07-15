def choose_best_sum(t, k, ls):
    from itertools import combinations
    comb=list(combinations(ls,k))                       #All possible combinations, k-length
    sums=[sum(i) for i in comb]                         #Sum of all combinations
    try:
        return max([i for i in sums if i <=t])          #Return biggest sum <= t
    except:
        return None                                     #Exception handling    
