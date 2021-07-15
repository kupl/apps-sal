import math

t = int(input())
while t:
    t -= 1
    n = int(input())
    l = input().split()
    l = [ int(i) for i in l ]
    print(math.ceil(n/min(l)))
