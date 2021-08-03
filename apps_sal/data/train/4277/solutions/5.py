def difference_in_ages(a):
    L = []
    L.append(min(a))
    L.append(max(a))
    L.append(max(a) - min(a))
    return tuple(L)
