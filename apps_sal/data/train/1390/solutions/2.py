import math

t = int(input())
while(t > 0):
    t -= 1
    p, q = list(map(int, input().split()))
    print('{:.10f}'.format(((p + q + 1) * q) / (q + 1)))
