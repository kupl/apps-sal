import sys


def readint():
    return int(sys.stdin.readline())


def readints():
    return tuple(map(int, sys.stdin.readline().split()))


def readintslist(n):
    return [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]


def main():
    (n, l) = readints()
    s = [input() for _ in range(n)]
    s = sorted(s)
    print(*s, sep='')


def __starting_point():
    main()


__starting_point()
