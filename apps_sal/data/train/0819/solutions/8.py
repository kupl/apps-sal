from fractions import gcd
t = int(input())
while t:
    (x, y) = [int(i) for i in input().split(' ')]
    if gcd(x, y) == 1:
        print('YES')
    else:
        print('NO')
    t -= 1
