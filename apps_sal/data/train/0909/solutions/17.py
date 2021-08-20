try:
    for _ in range(int(input())):
        n = int(input())
        b = list(map(int, input().split()))
        g = list(map(int, input().split()))
        b.sort()
        g.sort()
        i = 0
        (flag1, flag2) = (1, 1)
        new1 = []
        new2 = []
        while i < n:
            new1.append(b[i])
            new1.append(g[i])
            i += 1
        for i in range(1, len(new1)):
            if new1[i] < new1[i - 1]:
                flag1 = 0
                break
        i = 0
        while i < n:
            new2.append(g[i])
            new2.append(b[i])
            i += 1
        for i in range(1, len(new2)):
            if new2[i] < new2[i - 1]:
                flag2 = 0
                break
        if flag1 or flag2:
            print('YES')
        else:
            print('NO')
except:
    pass
