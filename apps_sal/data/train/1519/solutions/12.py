# cook your dish here
import math
t = int(input())
for i in range(t):
    x = int(input())
    n = math.floor(math.log2(x)) + 1
    if(x == 2**(n - 1)):
        print(x)
    else:
        print(2**n)
