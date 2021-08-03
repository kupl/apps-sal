from math import *
arr = []
for n in range(1, 11 + 1):
    v = int(input())
    arr = [v] + arr

for n in range(1, 11 + 1):
    J = arr.pop(0)
    temp = J
    a = sqrt(abs(temp))
    b = (temp**3) * 5
    r = a + b
    if r < 400:
        r = (str(round(r, 2)) + '0').split('.')
        r[1] = r[1][0:2]
        r = '.'.join(r)
        print(f"f({J}) = {r}")
    else:
        print(f"f({J}) = MAGNA NIMIS!")
