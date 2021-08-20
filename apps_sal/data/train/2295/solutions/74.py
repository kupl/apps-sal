n = int(input())
res = 10 ** 10
s = 0
l = [list(map(int, input().split())) for _ in range(n)]
for (a, b) in l:
    s += a
    if a > b:
        res = min(res, b)
if res == 10 ** 10:
    print(0)
else:
    print(s - res)
