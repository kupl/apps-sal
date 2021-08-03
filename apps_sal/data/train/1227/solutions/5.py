t = int(input())
for _ in range(t):
    s = input().split()
    d = {}
    for i in range(6):
        try:
            d[s[i]].append(i)
        except:
            d[s[i]] = [i]
    flag = False
    for i in list(d.keys()):
        if len(d[i]) >= 3:
            if 0 in d[i] or 1 in d[i]:
                if (3 in d[i] or 2 in d[i]) and (4 in d[i] or 5 in d[i]):
                    flag = True
                    break

    if flag:
        print('YES')
    else:
        print('NO')
