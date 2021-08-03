import math
for i in range(int(input())):
    l, b = list(map(int, input().split()))
    gcd1 = math.gcd(l, b)
    newl = (l // gcd1)
    new2 = (b // gcd1)
    print(newl * new2)
