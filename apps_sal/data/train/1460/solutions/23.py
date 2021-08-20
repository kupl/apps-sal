(d, x, y) = list(map(int, input().split()))
lis = list(map(int, input().split()))
ans = d * x
for i in range(d):
    while lis[i] > 1:
        y = y - 2 / 100 * y
        lis[i] = lis[i] - 1
    ans = ans + y
if ans < 300:
    print('NO')
else:
    print('YES')
