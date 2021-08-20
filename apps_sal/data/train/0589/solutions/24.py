t = int(input())
for i in range(t):
    s = str(input())
    l = []
    cou = 0
    for j in s:
        if j == '.':
            cou += 1
        elif cou != 0:
            l.append(cou)
            cou = 0
    if len(l) == 0:
        print(0)
    else:
        cou = l[0]
        ans = 1
        for j in l:
            if j > cou:
                ans += 1
                cou = j
        print(ans)
