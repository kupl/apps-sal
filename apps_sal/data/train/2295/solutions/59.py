
N = int(input())
AB = (list(map(int, input().split())) for _ in range(N))

INF = 10 ** 9 + 10
s = 0
last = INF
for a, b in AB:
    if a > b:
        last = min(last, b)
    s += b

if last == INF:
    print((0))
else:
    print((s - last))
