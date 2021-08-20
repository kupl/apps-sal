import math
tt = int(input())
for i in range(tt):
    n = int(input())
    a = n - math.ceil(n / 2)
    print(1, 10 ** a)
