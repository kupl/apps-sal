t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    f = {}
    poss = 1
    A = [[a[i], i] for i in range(n)]
    for i in range(n):
        if a[i] in f:
            f[a[i]] += 1
        else:
            f[a[i]] = 1
    for i in list(f.values()):
        if i > n // 2:
            poss = 0
    if poss:
        A.sort()
        ans = [0] * n
        j = max(f.values())
        B = A[j:] + A[:j]
        for i in range(n):
            ans[A[i][1]] = B[i][0]
        print('Yes')
        print(*ans)
    else:
        print('No')
