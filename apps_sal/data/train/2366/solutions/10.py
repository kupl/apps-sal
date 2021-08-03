from sys import stdin
t = int(stdin.readline().strip())
for j in range(t):
    n = int(stdin.readline().strip())
    s = list(map(int, stdin.readline().strip().split()))
    mn = s[-1]
    ans = 0
    for i in range(n - 2, -1, -1):
        if mn < s[i]:
            ans += 1
        mn = min(mn, s[i])
    print(ans)
