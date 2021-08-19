# cook your dish here
import math
t = int(input())
for _ in range(t):
    n = int(input())
    if math.ceil(math.log2(n)) == math.floor(math.log2(n)):
        print(0)
    else:
        x, c = 0, 0
        while n > 0:
            x = 2**math.floor(math.log2(n))
            c += 1
            n = n - x
            if math.ceil(math.log2(n)) == math.floor(math.log2(n)):
                break
        print(c)
