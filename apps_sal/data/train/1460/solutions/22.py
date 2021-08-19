(d, x, y) = list(map(int, input().split()))
ans = 0
for i in list(map(int, input().split())):
    ans += x
    v = y
    for j in range(i - 1):
        v = v - 2 * v / 100
    ans += v
if ans >= 300:
    print('YES')
else:
    print('NO')
