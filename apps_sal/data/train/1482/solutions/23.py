# cook your dish here
import math
tt = int(input())
for i in range(tt):
    n = int(input())
    b = math.ceil(n / 2)
    nu = 10**b
    de = 10**n
    q = math.gcd(nu, de)
    print(nu // q, de // q)
