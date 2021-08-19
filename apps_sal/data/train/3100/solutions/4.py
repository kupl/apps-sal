def max_and_min(lst1, lst2):
    diff = sorted((abs(b - a) for a in lst1 for b in lst2))
    return [diff[-1], diff[0]]
