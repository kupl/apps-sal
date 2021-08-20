for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input()]
    d = int(input())
    p = list(map(int, input().split()))
    narr = [l[0:p[0] - 1], l[p[0] - 1:]]
    for i in range(1, d + 1):
        for j in narr:
            t = 0
            while t < len(j):
                if j[t] == 1:
                    inner = 0
                    if t == 0 and len(j) > 1:
                        if j[t + 1] == 1:
                            inner = 1
                        j[t + 1] = 1
                    elif t == len(j) - 1:
                        j[t - 1] = 1
                    else:
                        if j[t + 1] == 1:
                            inner = 1
                        j[t + 1] = 1
                        j[t - 1] = 1
                    if t + 1 < len(j) and inner == 0:
                        t = t + 1
                t = t + 1
        if i == d:
            break
        now = p[i]
        no = 0
        tnarr = []
        flag = 0
        for j in narr:
            no += len(j)
            if no >= now and flag == 0:
                ind = no - len(j)
                ind = now - ind
                flag = 1
                tnarr.append(j[0:ind - 1])
                tnarr.append(j[ind - 1:])
            else:
                tnarr.append(j)
        narr = tnarr
    ctr = 0
    for i in narr:
        for j in i:
            if j == 1:
                ctr += 1
    print(ctr)
