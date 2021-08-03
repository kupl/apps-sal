def solve():
    n = int(input())
    a = list(map(int, input().split()))
    vis = [False] * (n + 1)
    p = []
    for i in a:
        if vis[i]:
            continue
        vis[i] = True
        p.append(i)
    print(*p)


t = int(input())
for _ in range(t):
    solve()
