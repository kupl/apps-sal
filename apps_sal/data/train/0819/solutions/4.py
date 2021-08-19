import math
for _ in range(int(input())):
    (x, y) = map(int, input().split())
    if math.gcd(x, y) == 1:
        print('YES')
        continue
    print('NO')
