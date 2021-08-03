t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    ans = s
    for i in range(n):
        x = s.copy()
        del(x[i])
        for j in range(n):
            ans = min(ans, x[:j] + [s[i]] + x[j:])
    print("".join(ans))
