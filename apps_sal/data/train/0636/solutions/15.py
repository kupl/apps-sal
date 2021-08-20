x = list(map(int, input().split()))
(n, t, a) = (x[0], x[1], x[2:])
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            for l in range(k + 1, n):
                if a[i] + a[j] + a[k] + a[l] == t:
                    ans += 1
print(ans)
