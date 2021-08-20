from sys import stdin
t = int(stdin.readline().strip())
for j in range(t):
    (n, m) = list(map(int, stdin.readline().strip().split()))
    vis = [False for i in range(10)]
    x = m % 10
    s = []
    while vis[x] != True:
        vis[x] = True
        s.append(x)
        x = (x + m) % 10
    y = n // m
    ans = 0
    z = y // len(s) * len(s)
    ans += sum(s) * (y // len(s))
    d = y - z
    for i in range(d):
        ans += s[i]
    print(ans)
