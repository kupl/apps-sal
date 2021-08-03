import math
for _ in range(int(input())):
    ab = input()
    a, b = list(map(int, ab.split(' ')))
    if a < b:
        a, b = (b, a)
    if math.gcd(a, b) > 1:
        print('NO')
    else:
        print('YES')
