for _ in range(int(input())):
    n, s = int(input()), input().strip()
    previ, num, _s, dic = s[0], 0, [], {}
    for i in s:
        if previ == i:
            num += 1
            continue
        _s.append((previ, num))
        if previ not in dic or dic[previ] < num:
            dic[previ] = num
        previ, num = i, 1
    _s.append((previ, num))
    if previ not in dic or dic[previ] < num:
        dic[previ] = num
    sum1 = sum(dic.values())
    del dic, s
    l, dicc = [i for (i, j) in _s], {}
    congr = [(l[i], l[i + 1]) for i in range(len(l) - 1)]
    for i in range(len(congr)):
        if congr[i] not in dicc:
            dicc[congr[i]] = set()
        dicc[congr[i]].add((_s[i][1], _s[i + 1][1]))
    sum2, ll = 0, []
    for i in dicc.keys():
        sortedset, deleted = sorted(list(dicc[i])), []
        for k in range(1, len(sortedset)):
            j = sortedset[k]
            if j[1] > sortedset[k - 1][1]:
                ind = k - 1
