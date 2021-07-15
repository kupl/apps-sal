n, d = map(int, input().split())
d += 1
t = list(map(int, input().split())) + [1000000001 + d]
s, j = 0, 2
for i in range(n - 2):
    while t[j] - t[i] < d: j += 1
    k = j - i - 1
    if k > 1: s += k *(k - 1)
print(s // 2)
