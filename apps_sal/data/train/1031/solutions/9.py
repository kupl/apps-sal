from math import sqrt
from sys import stdin


def solution(h, s):
    sqrt1 = h ** 4 - 16 * s ** 2
    if(sqrt1 < 0):
        return False
    sqrt2 = h**2 - sqrt(sqrt1)
    if(sqrt2 < 0):
        return False
    sqrt2 = sqrt(sqrt2 / 2)
    sqrt3 = h**2 + sqrt(sqrt1)
    sqrt3 = sqrt(sqrt3 / 2)
    return [sqrt2, sqrt3]


t = int(stdin.readline())
while t > 0:
    t -= 1
    h, s = list(map(int, stdin.readline().split()))
    answer = solution(h, s)
    if(answer == False):
        print(-1)
    else:
        answer.append(h)
        answer = sorted(answer)
        for i in answer:
            print(i, end=' ')
        print()
