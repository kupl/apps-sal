# cook your dish here
import math
t = int(input())
while(t):
    n1,k1 = input().split(" ")
    n = int(n1)
    k = int(k1)
    val = math.ceil(n/2)
    res = val*k
    print(res)
    t =t-1

