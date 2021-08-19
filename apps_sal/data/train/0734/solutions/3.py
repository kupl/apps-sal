from collections import Counter
tc = int(input())
while tc > 0:
    n = int(input())
    lis = list(map(int, input().split()))
    l1 = [(x, y) for (y, x) in enumerate(lis)]
    lis.sort()
    l1.sort()
    i = 0
    c_l = []
    while i < n:
        x = lis[i]
        j = 0
        c = 0
        while i + j < n and lis[i + j] == x:
            c += 1
            j += 1
        c_l.append(c)
        i += j
    c = max(c_l)
    if c > n // 2:
        print('No')
    else:
        ans = [0] * n
        for i in range(len(lis)):
            ans[l1[i][1]] = l1[i - c][0]
        print('Yes')
        print(*ans)
    tc -= 1
