# Python3 program to find XNOR
# of two numbers
import math


def swap(a, b):
    temp = a
    a = b
    b = temp


# log(n) solution
def xnor(a, b):
    # Make sure a is larger
    if (a < b):
        swap(a, b)

    if (a == 0 and b == 0):
        return 1

    # for last bit of a
    a_rem = 0

    # for last bit of b
    b_rem = 0

    # counter for count bit and
    # set bit in xnor num
    count = 0

    # for make new xnor number
    xnornum = 0

    # for set bits in new xnor
    # number
    while (a != 0):

        # get last bit of a
        a_rem = a & 1

        # get last bit of b
        b_rem = b & 1

        # Check if current two
        # bits are same
        if (a_rem == b_rem):
            xnornum |= (1 << count)

        # counter for count bit
        count = count + 1

        a = a >> 1
        b = b >> 1

    return xnornum


t = int(input())
for o in range(t):
    a, b, n = map(int, input().split())
    c = a ^ b
    x = bin(c)
    x = x.split("b")
    x = x[1]
    x = len(x)
    d = xnor(a, b)
    p = [a, b, c]
    r = [a, b, d]
    k = n % 3 - 1
    if p[k] > r[k]:
        print(p[k])
    else:
        print(r[k])
