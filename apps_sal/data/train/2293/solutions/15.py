n = int(input())
a = list(map(int, input().split()))
m = [[ai] for ai in a]
for d in range(n):
    for s in range(1 << n):
        if s >> d & 1 == 0:
            t = s | 1 << d
            m[t] = sorted(m[t] + m[s])[-2:]
for k in range(1, 1 << n):
    ans = sum(m[k])
    for d in range(n):
        if k >> d & 1 == 1:
            t = k ^ 1 << d  | (1 << d) - 1
            ans = max(ans, sum(m[t]))
    print(ans)
