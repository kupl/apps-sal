def main():
    import sys
    input = sys.stdin.readline

    def solve():
        n = int(input())
        maxx = 10**5
        minx = -10**5
        maxy = 10**5
        miny = -10**5

        for _ in range(n):
            x, y, f1, f2, f3, f4 = map(int, input().split())
            if not f1:
                minx = max(minx, x)
            if not f2:
                maxy = min(maxy, y)
            if not f3:
                maxx = min(maxx, x)
            if not f4:
                miny = max(miny, y)

        if minx > maxx or miny > maxy:
            print(0)
        else:
            print(1, minx, miny)

    for _ in range(int(input())):
        solve()

    return 0


main()
