t = int(input())
import math as m

for test in range(1, t+1):
    n = int(input())
    x = int(n**0.5)-1
    y = m.ceil(n/(x+1))
    print(x+y-1)

