def my_languages(A):
    L = []
    for i in A:
        if A.get(i) >= 60:
            L.append(A.get(i))
    L1 = []
    L.sort()
    L = L[::-1]
    for i in L:
        k = list(A.keys())
        v = list(A.values())
        b = k[v.index(i)]
        L1.append(b)
    return L1
