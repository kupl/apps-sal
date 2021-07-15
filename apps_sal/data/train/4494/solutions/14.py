def points(arr):
    L = []
    for i in arr:
        L1 = i.split(":")
        if L1[0] > L1[1]:
            L.append(3)
        elif L1[0] < L1[1]:
            L.append(0)
        elif L1[0] == L1[1]:
            L.append(1)
    return sum(L)
