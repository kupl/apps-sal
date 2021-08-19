import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        (n, sx, sy, dx, dy, bx, by) = list(map(int, sys.stdin.readline().strip().split()))
        if sx == bx == dx and min(sy, dy) < by and (by < max(sy, dy)):
            print(abs(dx - sx) + abs(dy - sy) + 2)
        elif sy == by == dy and min(sx, dx) < bx and (bx < max(sx, dx)):
            print(abs(dx - sx) + abs(dy - sy) + 2)
        else:
            print(abs(dx - sx) + abs(dy - sy))


main()
