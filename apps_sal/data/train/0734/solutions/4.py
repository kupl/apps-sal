for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l1 = [(x, i) for (i, x) in enumerate(l)]
    l.sort()
    l1.sort()
    i = 0
    count = []
    while i < n:
        x = l[i]
        j = 0
        c = 0
        while i + j < n and l[i + j] == x:
            c += 1
            j += 1
        count.append(c)
        i += j
    c = max(count)
    if c > n // 2:
        print('No')
    else:
        ans = [0] * n
        for i in range(len(l)):
            ans[l1[i][1]] = l1[i - c][0]
        print('Yes')
        print(*ans)
