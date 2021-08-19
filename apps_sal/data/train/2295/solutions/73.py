n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]
INF = 1 << 30
mx = INF
sm = 0
for i in range(n):
    (a, b) = ab[i]
    sm += a
    if a > b:
        mx = min(mx, b)
if mx == INF:
    print(0)
else:
    print(sm - mx)
