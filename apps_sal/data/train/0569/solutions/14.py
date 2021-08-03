# code
import math
t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    n -= 1
    n1 = (int(math.sqrt(8 * n + 1)) - 1) // 2
    i = n1 * (n1 + 1) // 2 - 1
    if(n1 + 1 + i == n):
        print(0)
    else:
        print(n - i)
