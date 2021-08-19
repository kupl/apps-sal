(n, s) = list(map(int, input().split(' ')))
aa = sorted(list(map(int, input().split(' '))))
res = 0
m = n // 2
for i in range(m):
    if aa[i] > s:
        res += aa[i] - s
res += abs(aa[m] - s)
for i in range(m + 1, n):
    if aa[i] < s:
        res += s - aa[i]
print(res)
