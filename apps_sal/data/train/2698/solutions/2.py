def sum_arrays(ar1, ar2):
    answ = []
    if not ar1 and not ar2:
        return []
    if not ar1:
        return ar2
    if not ar2:
        return ar1
    if ar1[0] == 0 and ar2[0] == 0:
        return []
    sa1 = "".join([str(k) for k in ar1])
    sa2 = "".join([str(j) for j in ar2])
    r = int(sa1) + int(sa2)
    if str(r)[0] == '-':
        for s in str(r)[1:]:
            answ.append(int(s))
        answ[0] *= -1
        return answ
    for s in str(r):
        answ.append(int(s))
    return answ
