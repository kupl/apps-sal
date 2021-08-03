# In the Name of God
import math

t = int(input())

for _ in range(t):
    z = input().split()
    x = int(z[0])
    r = int(z[1])
    a = int(z[2])
    b = int(z[3])
    length = 2 * math.pi * r
    if b > a:
        temp = a
        a = b
        b = temp
    first_meet = length / (a - b)
    total_time = (x * length) / a
    if(first_meet == total_time):
        ans = 0
    else:
        ans = int(total_time / first_meet)
    print(ans)
