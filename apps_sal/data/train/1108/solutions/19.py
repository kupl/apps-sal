(n, m, k) = map(int, input().split())
ans = 0
for i in range(n):
    temp = list(map(int, input().split()))
    su = 0
    for j in range(k):
        su += temp[j]
    if su >= m and temp[-1] <= 10:
        ans += 1
print(ans)
