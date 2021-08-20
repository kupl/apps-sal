t = int(input())
while t:
    t = t - 1
    n = list(map(int, input().split()))
    n.sort()
    x = n[0] ** 2 + n[1] ** 2
    if x == n[2] ** 2 and n[0] + n[1] > n[2] and (n[0] * n[1] * n[2] != 0):
        print('YES')
    else:
        print('NO')
