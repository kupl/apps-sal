def pair_of_shoes(a):
    return sorted(s for lr, s in a if lr == 1) == sorted(s for lr, s in a if lr == 0)
