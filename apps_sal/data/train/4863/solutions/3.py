def circularly_sorted(lst):
    std = sorted(lst)
    i = len(std) - 1 - std[::-1].index(lst[0])
    return std[i:] + std[:i] == lst
