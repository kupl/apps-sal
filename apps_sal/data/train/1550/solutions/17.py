import math


def xnor(a, b):
    if (a < b):
        a, b = b, a

    if (a == 0 and b == 0):
        return 1
    # for last bit of a
    a_rem = 0
    # for last bit of b
    b_rem = 0
    # counter for count bit and
    #  set bit in xnor num
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


for _ in range(int(input())):
    a, b, n = map(int, input().split())
    X = [a, b, a ^ b]
    E = [a, b, xnor(a, b)]

    i = (n - 1) % 3

    print(max(X[i], E[i]))
