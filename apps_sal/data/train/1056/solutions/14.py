def valid(a, b, c):
    if a + b + c == 180:
        print('YES')
    else:
        print('NO')


t = int(input())
while t:
    t = t - 1
    (a, b, c) = list(map(int, input().split()))
    valid(a, b, c)
