import sys


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 2)


line = sys.stdin.readline()
n = int(line)
while n:
    try:
        line = sys.stdin.readline()
        t = int(line)
    except:
        break
    x = fact((2 * t) - 1)
    print("%d\n" % x)
    n -= 1
