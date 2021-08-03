# cook your dish here
import math
t = int(input())
while t > 0:
    n, a, b, k = list(map(int, input().split()))
    l = (a * b) // math.gcd(a, b)
    c = n // b + n // a - 2 * (n // l)
    if c >= k:
        print("Win")
    else:
        print("Lose")
    t = t - 1
