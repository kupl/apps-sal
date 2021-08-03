# cook your dish here
import math
t = int(input())
for i in range(0, t):
    n, v1, v2 = input().split()
    n = int(n)
    v1 = int(v1)
    v2 = int(v2)
    time1 = n / v2 * 2
    time2 = math.sqrt(2) * n / v1
    if time1 <= time2:
        print("Elevator")
    else:
        print("Stairs")
