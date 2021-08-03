# cook your dish here
import math
a, b = map(int, input().split())
c = 0
for x in range(1, a + 1):
    for y in range(1, b + 1):
        if math.modf(math.sqrt(float(x * x) + float(y)))[0] == 0.0:
            c += 1
print(c)
