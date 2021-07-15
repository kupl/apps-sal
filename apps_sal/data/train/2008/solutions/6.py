n = int(input())
a = list(map(int, input().split()))
a = [a[0]] + a[:] + [a[-1]]
b = a[:]
cur = 0
ans = 0
c1 = c2 = -1
for i in range(1, n + 2):
    if a[i] != a[i - 1]:
        if cur == 0:
            c1 = a[i - 1]
        cur += 1
        ans = max(ans, cur // 2)
    elif cur:
        c2 = a[i - 1]
        if cur % 2 == 0:
            for j in range(i - cur, i - 1):
                b[j] = c1
        else:
            mid = i - (cur // 2) - 1
            for j in range(i - cur, i - 1):
                b[j] = c1 if j < mid else c2
        cur = 0
print(ans)
print(*b[1:-1])

