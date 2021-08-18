import sys


def _r(*conv):
    r = [conv[i](x) for i, x in enumerate(input().strip().split(' '))]
    return r[0] if len(r) == 1 else r


def _ra(conv):
    return list(map(conv, input().strip().split(' ')))


def _rl():
    return list(input().strip())


def _rs():
    return input().strip()


def _a(k, *v):
    return all(x == k for x in v)


def _i(conv):
    for line in sys.stdin:
        yield conv(line)


for _ in range(_r(int)):
    n, sx, sy, ex, ey, bx, by = _ra(int)

    if sx != ex and sy != ey:
        print(abs(sx - ex) + abs(sy - ey))
    else:
        if sx == ex:
            if sx == bx:
                if (by > sy and by < ey) or (by < sy and by > ey):
                    print(abs(sx - ex) + abs(sy - ey) + 2)
                else:
                    print(abs(sx - ex) + abs(sy - ey))
            else:
                print(abs(sx - ex) + abs(sy - ey))
        else:
            if sy == by:
                if (bx > sx and bx < ex) or (bx < sx and bx > ex):
                    print(abs(sx - ex) + abs(sy - ey) + 2)
                else:
                    print(abs(sx - ex) + abs(sy - ey))
            else:
                print(abs(sx - ex) + abs(sy - ey))
