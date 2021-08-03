for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    ans = [[0 for i in range(m)] for i in range(n)]
    k = 0
    if n == 1:
        for i in range(m):
            if i % 4 == 0 or i % 4 == 1:
                t = 1
            else:
                t = 2
            ans[0][i] = t
            k = max(k, ans[0][i])
    elif m == 1:
        for i in range(n):
            if i % 4 == 0 or i % 4 == 1:
                t = 1
            else:
                t = 2
            ans[i][0] = t
            k = max(k, ans[i][0])
    elif n == 2:
        t = 1
        for i in range(m):
            ans[0][i] = t
            ans[1][i] = t
            t = (t) % 3 + 1
            k = max(k, ans[0][i])
    elif m == 2:
        t = 1
        for i in range(n):
            ans[i][0] = t
            ans[i][1] = t
            t = t % 3 + 1
            k = max(k, ans[i][0])
    else:
        for i in range(n):
            if i % 4 == 0 or i % 4 == 1:
                t = 0
            else:
                t = 2
            for j in range(m):
                ans[i][j] = (t % 4) + 1
                t += 1
                k = max(k, ans[i][j])

    print(k)
    for i in range(n):
        print(*ans[i])
