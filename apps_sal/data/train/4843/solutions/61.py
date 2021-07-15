from itertools import combinations as cb
def choose_best_sum(t, k, ls):
    try:
        return max ([s for s in [sum(i) for i in cb(ls,k)] if s<=t])
    except:
        return None
