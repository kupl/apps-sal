USE_STDIO = False

if not USE_STDIO:
    try:
        import mypc
    except:
        pass


def main():
    n, = list(map(int, input().split(' ')))
    a = [x for x in map(int, input())]
    b = [x for x in map(int, input())]
    cnts = [0, 0, 0, 0]
    for x, y in zip(a, b):
        cnts[x * 2 + y] += 1
    ans = cnts[0] * cnts[3] + cnts[1] * cnts[2] + (cnts[0] * cnts[2])
    print(ans)


def __starting_point():
    main()


__starting_point()
