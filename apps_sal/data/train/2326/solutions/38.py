n = int(input())
a = list(map(int, input().split()))

b = sorted([(i + 1, a[i]) for i in range(n)], key=lambda x: -x[1])
ans = [0] * (n + 1)
m = float('inf')
for i in range(n - 1):
    m = min(m, b[i][0])
    if b[i][1] == b[i + 1][1]:
        continue
    ans[m] += (i + 1) * (b[i][1] - b[i + 1][1])
ans[1] += sum(a) - sum(ans)
for i in range(1, n + 1):
    print(ans[i])
