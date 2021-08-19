(N, T) = map(int, input().split())
xs = list(map(int, input().split()))
m = 10 ** 10
M = 0
ans = 1
for x in xs:
    if x < m:
        m = x
    elif x - m == M:
        ans += 1
    elif x - m > M:
        ans = 1
        M = x - m
print(ans)
