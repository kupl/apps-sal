import sys
sys.setrecursionlimit(10 ** 6)


def int1(x):
    return int(x) - 1


def p2D(x):
    return print(*x, sep='\n')


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def main():
    inf = 10 ** 10
    n = II()
    xy = [LI() for _ in range(n)]
    xy = [[x, y] if x < y else [y, x] for (x, y) in xy]
    xy.sort()
    yy = [y for (x, y) in xy]
    xmin = xy[0][0]
    xmax = xy[-1][0]
    ymax = max(yy)
    ymin = min(yy)
    ans = (xmax - xmin) * (ymax - ymin)
    d = ymax - xmin
    ymin = inf
    for i in range(n - 1):
        y = xy[i][1]
        if y < ymin:
            ymin = y
        xmin = min(xy[i + 1][0], ymin)
        xmax = max(xmax, y)
        ans = min(ans, (xmax - xmin) * d)
    print(ans)


main()
