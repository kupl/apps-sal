import sys

cin = sys.stdin


def getInts():
    return list(map(int, cin.readline().rstrip("\n").split(" ")))


t = getInts()[0]
while t:
    n, q = getInts()
    res = q + (n * q) / (q + 1)
    print(res)
    t -= 1
