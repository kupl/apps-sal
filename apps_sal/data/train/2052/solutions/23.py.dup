n, m = map(int, input().split())
ans = 0
row = [1] * n * 2
for x in range(m):
    a, b = [int(x) for x in input().split()]
    row[a - 1] = 0
    row[b - 1 + n] = 0

for i in range(1, (n + 1) // 2):
    j = n - 1 - i
    if i == j:
        ans += min(1, row[i] + row[i + n])
    else:
        ans += row[i] + row[j] + row[i + n] + row[j + n]
print(ans)
