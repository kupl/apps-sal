# cook your dish here
import math
a, b = list(map(int, input().split()))
c = 0
for i in range(1, a + 1):
    for j in range(1, b + 1):
        n = i**2 + j
        sr = math.sqrt(n)
        if(sr - math.floor(sr) == 0):
            c += 1
print(c)
