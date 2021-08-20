import math
for _ in range(int(input())):
    (x, y) = list(map(int, input().split()))
    r = 1
    b = 1
    temp = math.gcd(x, y)
    if temp == 1:
        print('YES')
    else:
        print('NO')
