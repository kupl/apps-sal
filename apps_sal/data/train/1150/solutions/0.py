import math
for _ in range(int(input())):
    n = int(input())
    c = 0
    while(n > 0):
        i = int(math.sqrt(n))
        c += 1
        n = n - i**2
    print(c)
