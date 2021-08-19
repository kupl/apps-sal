import math
t = int(input())
for _ in range(t):
    n = int(input())
    x = math.floor((-1 + math.sqrt(1 + 8 * n)) // 2)
    num = x * (x + 1) // 2
    print(n - num)
