def twos_difference(lst):
    if not lst:
        return []
    test = list(range(min(lst), max(lst) + 1))
    return [(test[i], test[i + 2]) for i in range(len(test) - 2) if all((test[i] in lst, test[i + 2] in lst))]
