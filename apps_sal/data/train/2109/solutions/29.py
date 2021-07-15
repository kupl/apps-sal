# seishin.py
from math import sqrt
Q = int(input())
for i in range(Q):
    a, b = map(int, input().split())
    if not a < b:
        a, b = b, a
    if a == b or a+1 == b:
        print(2*a-2)
        continue
    c = int(sqrt(a*b))
    if c**2 == a*b:
        c -= 1
    if c*(c+1) >= a*b:
        print(2*c-2)
        continue
    print(2*c-1)
