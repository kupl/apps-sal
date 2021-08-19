def bubble(l):
    ret = []
    for i in range(len(l) - 1, 0, -1):
        for j in range(i):
            if l[j] > l[j + 1]:
                (l[j], l[j + 1]) = (l[j + 1], l[j])
                ret.append(l[:])
    return ret
