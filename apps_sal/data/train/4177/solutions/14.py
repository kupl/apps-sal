def men_from_boys(arr):
    L = []
    L1 = []
    for i in arr:
        if i % 2 == 0:
            if i not in L:
                L.append(i)
        elif i not in L1:
            L1.append(i)
    L.sort()
    L1.sort()
    L1 = L1[::-1]
    return L + L1
