t = int(input())
for i in range(0, t):
    x = list(map(int, input().split()))
    x.sort()
    if x[2] ** 2 == x[0] ** 2 + x[1] ** 2 and x[0] != 0:
        print('YES')
    else:
        print('NO')
