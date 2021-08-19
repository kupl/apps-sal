import math
for i in range(int(input())):
    (a, b) = list(map(int, input().split()))
    if math.gcd(a, b) == 1:
        print('YES')
    else:
        print('NO')
