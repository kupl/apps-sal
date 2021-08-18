import math


def check(s):
    if s == 2:
        return 1

    for i in range(2, math.ceil(math.sqrt(s)) + 1):
        if s % i == 0:
            return 0

    return 1


def Solve(slots):
    if slots < 3:
        return 0

    s = math.sqrt(slots)
    if math.floor(s) == math.ceil(s):
        return check(s)

    return 0


N = int(input())

for t in range(N):

    slots = int(input())

    if (Solve(slots)):
        print("YES")

    else:
        print("NO")
