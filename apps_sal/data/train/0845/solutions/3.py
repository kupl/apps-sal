import math
for _ in range(int(input())):
    (a, b) = map(int, input().split())
    _gcd = math.gcd(a, b)
    tmp = a * b // (_gcd * _gcd)
    print(tmp)
