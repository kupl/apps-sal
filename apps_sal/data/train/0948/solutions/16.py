# cook your dish here
import math
a, b = map(int, input().split())
c = 0
for i in range(2, int(math.sqrt(a * a + b)) + 1):
    for x in range(1, i):
        if x > a:
            break
        c += int(i * i - x * x <= b)
print(c)
