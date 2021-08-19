# cook your dish here
import math


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) // gcd(a, b)


t = int(input())
while(t > 0):
    n, a, b, k = map(int, input().split())
    prob = 0

    rem1 = n // a
    rem2 = n // b
    if a >= b:
        rem3 = n // lcm(b, a)
    else:
        rem3 = n // lcm(a, b)
    res = (rem1 - rem3) + (rem2 - rem3)
    if(res < k):
        print("Lose")
    else:
        print("Win")
    t -= 1
