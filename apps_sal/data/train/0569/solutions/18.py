import math
t = int(input())
for i in range(0, t):
    n = int(input())
    k = 0
    x = 0
    k = ((int(math.sqrt(((8 * n) + 1))) - 1) // 2)
    x = (k * (k + 1) // 2)
    n = n - x
    print(n)
