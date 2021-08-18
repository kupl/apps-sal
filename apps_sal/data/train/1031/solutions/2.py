from math import sqrt
from math import pow

t = int(input())

while(t > 0):
    t = t - 1
    h, s = list(map(int, input().split()))
    s2 = pow(s, 2)
    h4 = pow(h, 4)
    s216 = s2 * 16
    sq2 = h4 - s216
    if(sq2 < 0):
        print("-1")
        continue
    sq = sqrt(sq2)
    hpsq = pow(h, 2) + sq
    a2 = hpsq / 2
    a = sqrt(a2)
    b2 = pow(h, 2) - a2
    b = sqrt(b2)
    if(a < b):
        print(str(a) + " ", str(b) + " ", str(h) + " ")
    else:
        print(str(b) + " ", str(a) + " ", str(h) + " ")
