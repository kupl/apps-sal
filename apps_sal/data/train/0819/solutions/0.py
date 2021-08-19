T = int(input())
while T:
    (x, y) = map(int, input().split())
    while y:
        (x, y) = (y, x % y)
    if x == 1:
        print('YES')
    else:
        print('NO')
    T -= 1
