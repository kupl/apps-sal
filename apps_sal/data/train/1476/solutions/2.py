from collections import Counter
import math

tc = int(input())
while tc > 0:
    s = input()
    k = math.factorial(s.__len__())
    x = Counter(s)
    for val in x.values():
        if val > 1:
            k = k // math.factorial(val)
    k = int(k)
    k = k % (10**9 + 7)
    print(k)
    tc -= 1
