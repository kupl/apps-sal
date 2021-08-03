n = int(input())
s = 0
minb = float("inf")
f = False
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        f = True
        minb = min(b, minb)
    s += a
if f:
    print(s - minb)
else:
    print(0)
