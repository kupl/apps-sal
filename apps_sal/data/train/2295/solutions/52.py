n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
(a, _) = list(zip(*ab))
sm = sum(a)
ans = 0
for (a, b) in ab:
    if a > b:
        ans = max(ans, sm - b)
print(ans)
