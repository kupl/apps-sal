t = int(input())
while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    s = list(set(a))
    s.sort()
    ind = dict()
    for i in range(n):
        if a[i] in ind:
            ind[a[i]].append(i)
        else:
            ind[a[i]] = [i]
    s1 = 1
    ref = -1
    for i in s:
        flag = 0
        for j in ind[i]:
            if j > ref:
                ref = j
                flag = 1
                break
        if flag == 0:
            s1 += 1
            ref = ind[i][0]
    print(s1)
