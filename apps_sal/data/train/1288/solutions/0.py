t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    mat = [0 for i in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u, v = (u - 1), (v - 1)
        mat[u] |= (1 << v)
        mat[v] |= (1 << u)
    for i in range(n):
        mat[i] |= (1 << i)

    goal = (2**n) - 1
    ans = n

    for i in range(1, goal + 1):
        mvs = 0
        loc = 0
        for j in range(n):
            if(i & (1 << j)):
                loc |= mat[j]
                mvs += 1
        if(loc == goal):
            ans = min(mvs, ans)
    print(ans)
