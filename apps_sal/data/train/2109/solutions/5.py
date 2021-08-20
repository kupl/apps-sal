import math


def __starting_point():
    q = int(input())
    for i in range(q):
        (a, b) = list(map(int, input().split()))
        prod = a * b
        rootInt = int(math.sqrt(prod))
        if a == b:
            print((a - 1) * 2)
        elif math.sqrt(prod) == rootInt:
            print((rootInt - 2) * 2 + 1)
        elif rootInt * (rootInt + 1) < prod:
            print((rootInt - 1) * 2 + 1)
        else:
            print((rootInt - 1) * 2)


__starting_point()
