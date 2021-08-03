def greatest_product(n):
    L = []
    L1 = []
    for i in n:
        L.append(int(i))
    for i in range(len(L) - 4):
        a = (L[i]) * (L[i + 1]) * (L[i + 2]) * (L[i + 3]) * (L[i + 4])
        L1.append(a)
    return max(L1)
