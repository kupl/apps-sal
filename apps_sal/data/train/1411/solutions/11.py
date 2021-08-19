from math import pi as p
from math import gcd, ceil
t = int(input())
while t > 0:
    t -= 1
    x, r, a, b = map(int, input().split())
    cir = 2 * p * r
    t1 = cir / a
    t2 = cir / b
    tf = cir / abs(a - b)
    s = min(t1, t2) * x
    s = s / tf
    # op = (min(t1,t2)*x)//tf
    s = ceil(s)
    print(s - 1)
