import math
for i in range(int(input().strip())):
    a, b = [int(i) for i in input().strip().split(' ')]
    if math.gcd(a, b) == 1:
        print('YES')
    else:
        print('NO')
