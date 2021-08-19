import sys
from collections import deque


def di(x, y, z, w):
    return abs(x - z) + abs(y - w)


def convert(a, b, c, d, e, f):
    if di(c, d, a, b) == 1 and di(c, d, e, f) == 1:
        a, b, c, d = c, d, a, b
    elif di(e, f, c, d) == 1 and di(e, f, a, b) == 1:
        a, b, e, f = e, f, a, b
    if c == a:
        if d == b + 1:
            if e == a + 1:
                a, b, c, d, e, f = a, b, a + 1, b, a, b + 1
            else:
                a, b, c, d, e, f = a, b, a, b + 1, a - 1, b
        else:
            if e == a + 1:
                a, b, c, d, e, f = a, b, a + 1, b, a, b - 1
            else:
                a, b, c, d, e, f = a, b, a - 1, b, a, b - 1
    elif c == a + 1:
        if f == b + 1:
            a, b, c, d, e, f = a, b, a + 1, b, a, b + 1
        else:
            a, b, c, d, e, f = a, b, a + 1, b, a, b - 1
    else:
        if f == b + 1:
            a, b, c, d, e, f = a, b, a, b + 1, a - 1, b
        else:
            a, b, c, d, e, f = a, b, a - 1, b, a, b - 1
    return (a, b, c, d, e, f)


dist = {}
pos = (0, 0, 1, 0, 0, 1)
deq = deque([pos])
dist[pos] = 0
while deq:
    a, b, c, d, e, f = deq.popleft()
    D = dist[a, b, c, d, e, f]
    if D == 10:
        continue

    nx, ny = 1, 1

    if (c, d) == (a + 1, b) and (e, f) == (a + 1, b):
        nx, ny = 1, 1
    elif (c, d) == (a, b + 1) and (e, f) == (a - 1, b):
        nx, ny = -1, 1
        c, d, e, f = e, f, c, d
    elif (c, d) == (a - 1, b) and (e, f) == (a, b - 1):
        nx, ny = -1, -1
    elif (c, d) == (a + 1, b) and (e, f) == (a, b - 1):
        nx, ny = 1, -1

    if convert(a + nx, b + ny, e, f, c, d) not in dist:
        dist[convert(a + nx, b + ny, e, f, c, d)] = D + 1
        deq.append(convert(a + nx, b + ny, e, f, c, d))

    if convert(e, f, e - nx, f, a, b) not in dist:
        dist[convert(e, f, e - nx, f, a, b)] = D + 1
        deq.append(convert(e, f, e - nx, f, a, b))
    if convert(a, b, e, f, a - nx, b) not in dist:
        dist[convert(a, b, e, f, a - nx, b)] = D + 1
        deq.append(convert(a, b, e, f, a - nx, b))
    if convert(e, f, e + nx, f, a, b) not in dist:
        dist[convert(e, f, e + nx, f, a, b)] = D + 1
        deq.append(convert(e, f, e + nx, f, a, b))

    if convert(c, d, a, b, c, d - ny) not in dist:
        dist[convert(c, d, a, b, c, d - ny)] = D + 1
        deq.append(convert(c, d, a, b, c, d - ny))
    if convert(a, b, c, d, a, b - ny) not in dist:
        dist[convert(a, b, c, d, a, b - ny)] = D + 1
        deq.append(convert(a, b, c, d, a, b - ny))
    if convert(c, d, c, d + ny, a, b) not in dist:
        dist[convert(c, d, c, d + ny, a, b)] = D + 1
        deq.append(convert(c, d, c, d + ny, a, b))

# print(dist)
# return


input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    a, b, c, d, e, f = map(int, input().split())
    if di(c, d, a, b) == 1 and di(c, d, e, f) == 1:
        a, b, c, d = c, d, a, b
    elif di(e, f, c, d) == 1 and di(e, f, a, b) == 1:
        a, b, e, f = e, f, a, b
    if c == a:
        if d == b + 1:
            if e == a + 1:
                a, b, c, d, e, f = a, b, a + 1, b, a, b + 1
            else:
                a, b, c, d, e, f = a, b, a, b + 1, a - 1, b
        else:
            if e == a + 1:
                a, b, c, d, e, f = a, b, a + 1, b, a, b - 1
            else:
                a, b, c, d, e, f = a, b, a - 1, b, a, b - 1
    elif c == a + 1:
        if f == b + 1:
            a, b, c, d, e, f = a, b, a + 1, b, a, b + 1
        else:
            a, b, c, d, e, f = a, b, a + 1, b, a, b - 1
    else:
        if f == b + 1:
            a, b, c, d, e, f = a, b, a, b + 1, a - 1, b
        else:
            a, b, c, d, e, f = a, b, a - 1, b, a, b - 1

    res = 10**18

    if (c, d, e, f) == (a + 1, b, a, b + 1):
        if a * b >= 0 and a and a == b:
            res = 2 * max(abs(a), abs(b)) + 1
        else:
            res = 2 * max(abs(a), abs(b))
    elif (c, d, e, f) == (a, b + 1, a - 1, b):
        if a >= 0 and b >= 0:
            if (a, b) == (0, 0):
                res = 1
            elif b >= a:
                res = 2 * b
            else:
                res = 2 * a - 1
        elif a >= 0 and b < 0:
            if -b >= a:
                res = 2 * -b
            else:
                res = 2 * a - 1
        elif a < 0 and b >= 0:
            if b > -a:
                res = 2 * b
            else:
                res = 2 * (-a) + 1
        else:
            if -b > -a:
                res = 2 * -b
            else:
                res = 2 * (-a) + 1
    elif (c, d, e, f) == (a + 1, b, a, b - 1):
        if a >= 0 and b >= 0:
            if (a, b) == (0, 0):
                res = 1
            elif a >= b:
                res = 2 * a
            else:
                res = 2 * b - 1
        elif a >= 0 and b < 0:
            if a > -b:
                res = 2 * a
            else:
                res = 2 * (-b) + 1
        elif a < 0 and b >= 0:
            if -a >= b:
                res = 2 * (-a)
            else:
                res = 2 * b - 1
        else:
            if -a > -b:
                res = 2 * (-a)
            else:
                res = 2 * (-b) + 1
    else:
        if a >= 0 and b >= 0:
            if (a, b) == (0, 0):
                res = 2
            elif b > a:
                res = 2 * b - 1
            elif a > b:
                res = 2 * a - 1
            else:
                if a == 1:
                    res = 1
                else:
                    res = 2 * a
        elif a >= 0 and b < 0:
            if -b >= a:
                res = 2 * (-b) + 1
            else:
                res = 2 * a - 1
        elif a < 0 and b >= 0:
            if -a >= b:
                res = 2 * (-a) + 1
            else:
                res = 2 * b - 1
        else:
            if a != b:
                res = 2 * max(-a, -b) + 1
            else:
                res = 2 + 2 * abs(a)
    ans.append(res)

print(*ans, sep="\n")
