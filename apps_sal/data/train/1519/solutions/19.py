import math


def exp(x):
    return x > 0 and (x & (x - 1)) == 0


def count(number):
    return int((math.log(number) // math.log(2)) + 1)


for x in range(int(input())):
    x = int(input())
    a = exp(x)
    if a == True:
        print(x)
    else:
        b = count(x)
        print(2**b)
