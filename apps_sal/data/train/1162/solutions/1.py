from sys import stdin


def getInt():
    return int(stdin.readline())


def getInts():
    return [int(z) for z in stdin.readline().split()]


for case in range(getInt()):
    N = getInt()
    while ((N >= 0) and ((N % 7) != 0)):
        N -= 4
    if (N < 0):
        N = -1
    print(N)
