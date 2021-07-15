def largest_pair_sum(a): 
    return a.pop(a.index(max(a))) + a.pop(a.index(max(a)))
