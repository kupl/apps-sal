(n, t) = list(map(int, input().split()))
a = list(map(int, input().split()))
m = a[-1]
tmp = 0
cnt = 0
for i in range(n - 2, -1, -1):
    p = m - a[i]
    if p > tmp:
        tmp = p
        cnt = 1
    elif p == tmp:
        cnt += 1
    m = max(m, a[i])
print(cnt)
