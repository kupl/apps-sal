t = eval(input())
for i in range(0, t):
    (n, m) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    (x, y) = (0, 0)
    for j in range(0, m):
        x = x + a[j]
    for j in range(m, n):
        y = y + a[j] / 2 + a[j] % 2
    if x >= y:
        print('VICTORY')
    else:
        print('DEFEAT')
