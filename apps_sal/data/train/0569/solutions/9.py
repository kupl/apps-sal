import math

t = int(input())

for _ in range(t):
    n = int(input())
    x = int(math.sqrt(2 * n))
    while(((x * (x + 1)) // 2) - 1 >= n):
        x -= 1
    ini = (x * (x + 1)) // 2
    ini -= 1
    print(int(n - ini - 1))
