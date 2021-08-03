# just code here
import math


def isPerfectSquare(x):

    # Find floating point value of
    # square root of x.
    sr = math.sqrt(x)

    # If square root is an integer
    return ((sr - math.floor(sr)) == 0)


a, b = list(map(int, input().split()))
c = 0
for i in range(1, a + 1):
    for j in range(1, b + 1):
        s = (i * i + j)
        if isPerfectSquare(s):
            c += 1
print(c)
