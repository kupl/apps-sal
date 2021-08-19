import sys
import math
import collections
import heapq
import itertools
F = sys.stdin


def single_input():
    return F.readline().strip('\n')


def line_input():
    return F.readline().strip('\n').split()


def solve():
    (R, C, N) = map(int, line_input())
    (u, l, r, d) = ([], [], [], [])
    for i in range(N):
        (x, y, z, w) = map(int, line_input())
        if x == 0:
            if z == 0:
                u.append((y, i))
                u.append((w, i))
            elif w == C:
                u.append((y, i))
                r.append((z, i))
            elif z == R:
                u.append((y, i))
                d.append((w, i))
            elif w == 0:
                u.append((y, i))
                l.append((z, i))
        elif x == R:
            if z == 0:
                d.append((y, i))
                u.append((w, i))
            elif w == C:
                d.append((y, i))
                r.append((z, i))
            elif z == R:
                d.append((y, i))
                d.append((w, i))
            elif w == 0:
                d.append((y, i))
                l.append((z, i))
        elif y == 0:
            if z == 0:
                l.append((x, i))
                u.append((w, i))
            elif w == C:
                l.append((x, i))
                r.append((z, i))
            elif z == R:
                l.append((x, i))
                d.append((w, i))
            elif w == 0:
                l.append((x, i))
                l.append((z, i))
        elif y == C:
            if z == 0:
                r.append((x, i))
                u.append((w, i))
            elif w == C:
                r.append((x, i))
                r.append((z, i))
            elif z == R:
                r.append((x, i))
                d.append((w, i))
            elif w == 0:
                r.append((x, i))
                l.append((z, i))
    u.sort()
    r.sort()
    d.sort(reverse=True)
    l.sort(reverse=True)
    s = []
    used = set()
    crossed = True
    for (point, n) in u:
        if n not in used:
            s.append(n)
            used |= {n}
        elif s[-1] != n:
            break
        else:
            s.pop()
    else:
        for (point, n) in r:
            if n not in used:
                s.append(n)
                used |= {n}
            elif s[-1] != n:
                break
            else:
                s.pop()
        else:
            for (point, n) in d:
                if n not in used:
                    s.append(n)
                    used |= {n}
                elif s[-1] != n:
                    break
                else:
                    s.pop()
            else:
                for (point, n) in l:
                    if n not in used:
                        s.append(n)
                        used |= {n}
                    elif s[-1] != n:
                        break
                    else:
                        s.pop()
                else:
                    crossed = False
    print('NO' if crossed else 'YES')
    return 0


def __starting_point():
    solve()


__starting_point()
