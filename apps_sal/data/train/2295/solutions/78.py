n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
sm = 0
bmin = 10 ** 10
for itm in ab:
    (a, b) = itm
    sm += a
    if a > b:
        bmin = min(bmin, b)
if bmin == 10 ** 10:
    print(0)
else:
    print(sm - bmin)
