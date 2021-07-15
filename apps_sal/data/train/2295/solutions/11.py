n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
m = pow(10, 18)
s = 0
for i in range(n):
    s += ab[i][0]
    if ab[i][0] > ab[i][1]:
        m = min(m, ab[i][1])
ans = max(0, s - m)
print(ans)
