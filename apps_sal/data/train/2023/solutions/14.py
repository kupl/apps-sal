n = int(input())
import math
d = int(math.sqrt(n))
for i in range(n // d):
    b = n - d * (i + 1) + 1
    for i in range(d):
        print(b, end = ' ')
        b += 1
a = 1
for i in range(n - d * (n // d)):
    print(a, end = ' ')
    a += 1

