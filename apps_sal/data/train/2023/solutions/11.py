import math
n = int(input())
x = math.ceil(math.sqrt(n))
y = n // x
for i in range(y):
    for j in range(x, 0, -1):
        print(j + i * x, end=' ')
for i in range(n, x * y, -1):
    print(i, end=' ')
