USE_STDIO = False

if not USE_STDIO:
    try:
        import mypc
    except:
        pass


def main():
    n, = list(map(int, input().split(' ')))
    q = int(n ** 0.5)
    ans = [i for i in range(1, n + 1)]
    for i in range(0, n, q):
        ans[i:i + q] = ans[i:i + q][::-1]
    print(*ans)


def __starting_point():
    main()


__starting_point()
