import math


def fun(num1, num2):
    if num1 > num2:
        a = num1
        b = num2
    else:
        a = num2
        b = num1
    rem = a % b
    while(rem != 0):
        a = b
        b = rem
        rem = a % b
    gcd = b
    return (int((num1 * num2) / gcd))


for _ in range(int(input())):
    hours = int(input()) * 24
    x, y, z = list(map(int, input().split()))
    lcm = x
    lcm = fun(x, y)
    lcm = fun(lcm, z)
    print(int(hours // lcm))
