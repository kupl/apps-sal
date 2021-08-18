from collections import deque
import sys


def MI(): return list(map(int, sys.stdin.readline().split()))


class water:
    def __init__(self, t, v):
        self.v = v
        self.tv = v * t

    def __le__(self, other):
        return self.v * other.tv - self.tv * other.v >= 0

    def __isub__(self, other):
        t = self.tv / self.v
        self.v -= other
        self.tv = t * self.v
        return self

    def __iadd__(self, other):
        self.v += other.v
        self.tv += other.tv
        return self


def main():
    n, l = MI()
    dam = deque()
    t, v = MI()
    print(t)
    dam.append(water(t, v))
    stv = t * v
    for _ in range(n - 1):
        t, v = MI()
        dam.appendleft(water(t, v))
        over = v
        stv += t * v
        while dam[-1].v <= over:
            w = dam.pop()
            over -= w.v
            stv -= w.tv
        stv -= dam[-1].tv
        dam[-1] -= over
        stv += dam[-1].tv
        print((stv / l))
        while len(dam) > 1 and dam[0] <= dam[1]:
            w = dam.popleft()
            dam[0] += w


main()
