def add_all(lst):
    if len(lst) == 1:
        return 0
    
    lst.sort()
    cost = sum(lst[:2])
    lst[:2] = cost,
    
    return cost + add_all(lst)

