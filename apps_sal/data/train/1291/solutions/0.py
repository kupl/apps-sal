import sys
DIRS = dict(U=(0, 1), D=(0, -1), R=(1, 0), L=(-1, 0))
KOEF = 0.2


def div(a, b):
    return round(float(a) / b, 1)


def collide_coord(ex, edx, x, dx):
    d = abs(ex - x)
    d2 = abs(ex + edx - x)
    d3 = abs(ex - x - dx)
    if d2 > d or d3 > d:
        return False
    d_next = abs(ex + edx * KOEF - x - dx * KOEF)
    speed = abs(d_next - d)
    if speed == 0:
        if ex != x:
            return
        return 'all'
    else:
        return div(d, speed / KOEF)


def main():
    t = int(input())
    for _ in range(t):
        (ex, ey, dir) = sys.stdin.readline().strip().split()
        ex = int(ex)
        ey = int(ey)
        (edx, edy) = DIRS[dir]
        n = int(sys.stdin.readline())
        min_time = float('+inf')
        for _ in range(n):
            (x, y, dir) = sys.stdin.readline().strip().split()
            x = int(x)
            y = int(y)
            (dx, dy) = DIRS[dir]
            tx = collide_coord(ex, edx, x, dx)
            if tx is False:
                continue
            ty = collide_coord(ey, edy, y, dy)
            if ty is False:
                continue
            if tx == 'all':
                min_time = min(min_time, ty)
            elif ty == 'all':
                min_time = min(min_time, tx)
            elif tx == ty:
                min_time = min(min_time, tx)
        print(min_time if min_time < 1000000 else 'SAFE')


def __starting_point():
    main()


__starting_point()
