n = int(input())
res = 100000000000000000000000
s = 0
f = 0
for i in range(n):
    (a, b) = list(map(int, input().split()))
    s += a
    if a > b:
        res = min(res, b)
    if a != b:
        f = 1
if not f:
    print(0)
else:
    print(s - res)
