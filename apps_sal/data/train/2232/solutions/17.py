import math

n = int(input())
x = 2
for i in range(1, n + 1):
    y = i * (i + 1)
    y *= y
    print(round((y - x) / i))
    x = math.sqrt(y)
