# cook your dish here
import math
n = int(input())
for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    x = math.gcd(a, b)
    y = (a * b) // x
    print(x, y)

    # if n1>n2:
    #     large = n1
    #     small = n2
    # else:
    #     large = n2
    #     small = n1
    # lt = large
    # st = small
    # while(st!=0):
    #     if small%st == 0 and large%st == 0:
    #         break
    #     else:
    #         st = st - 1
