def maxlen(L1,L2):
    if L1 > L2 and L1 / 3 > L2:
        return L1 / 3
    elif L2 > L1 and L2 / 3 > L1:
        return L2 / 3
    elif L1 > L2 and L1 / 2 > L2:
        return L2
    elif L2 > L1 and L2 / 2 > L1:
        return L1
    elif L1 > L2 and L1 / 2 < L2:
        return L1 / 2
    elif L2 > L1 and L2 / 2 < L1:
        return L2 / 2
