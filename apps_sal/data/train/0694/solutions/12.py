import math
from math import gcd


def prime(n):
    if n <= 1:
        return False
    max_div = math.floor(math.sqrt(n))
    for i in range(2, 1 + max_div):
        if n % i == 0:
            return False
    return True


t = int(input())
for rr in range(t):
    n = int(input()) * 24
    (x, y, z) = list(map(int, input().split(' ')))

    def find_lcm(num1, num2):
        if num1 > num2:
            num = num1
            den = num2
        else:
            num = num2
            den = num1
        rem = num % den
        while rem != 0:
            num = den
            den = rem
            rem = num % den
        gcd = den
        lcm = int(int(num1 * num2) / int(gcd))
        return lcm
    l = [x, y, z]
    num1 = l[0]
    num2 = l[1]
    lcm = find_lcm(num1, num2)
    for i in range(2, len(l)):
        lcm = find_lcm(lcm, l[i])
    print(n // lcm)
