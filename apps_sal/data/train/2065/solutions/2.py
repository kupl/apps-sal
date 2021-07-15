import sys

n, k = list(map(int, sys.stdin.readline().split()))
ans, pref = 0, 0
for i in range(k):
    m, *a = list(map(int, sys.stdin.readline().split()))
    j = 0
    while j < m and a[j] == j + 1:
        j += 1
    if j:
        pref = j
        ans += m - j
    else:
        ans += m - 1
print(ans + n - pref)

