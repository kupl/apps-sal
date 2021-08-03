def modified_sum(a, n):
    L = []
    for i in a:
        L.append(i**n)
    return sum(L) - sum(a)
