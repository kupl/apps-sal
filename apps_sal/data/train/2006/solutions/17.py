
from math import gcd

n = int(input())
ar = sorted(map(int, input().split()))

d = gcd(ar[0], ar[1])

for i in range(2, n):
    d = gcd(d, ar[i])

N = max(ar) // d - n
print("Alice" if N % 2 else "Bob")


#  C:\Users\Usuario\HOME2\Programacion\ACM
