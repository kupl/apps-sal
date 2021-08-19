(n, d) = map(int, input().split())
x = list(map(int, input().split()))
(j, v) = (0, 0)
for i in range(n - 2):
    while j < n - 1 and x[j + 1] - x[i] <= d:
        j += 1
    v += (j - i) * (j - i - 1) // 2
print(v)
