import itertools
def choose_best_sum(t, k, ls):
#create a list of all combinations of ls of length k
    combinations = itertools.combinations(ls, k)
    a=list(combinations)
#sum all items in list
    b=[sum(c) for c in a]
#select maximum in list
    d=[i for i in b if i <= t]
    if not d:
        return (None)
    else:
        d_max = max(d)
        return(d_max)
