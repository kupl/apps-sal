def main():
    # input data
    import sys
    def input(): return sys.stdin.readline().strip()
    n, a, b = map(int, input().split())
    x = list(map(int, input().split()))

    # solve
    ans = 0
    for i in range(n - 1):
        if (x[i + 1] - x[i]) * a > b:
            ans += b
        else:
            ans += (x[i + 1] - x[i]) * a
    print(ans)


def __starting_point():
    main()


__starting_point()
