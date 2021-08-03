def main():
    n = int(input())
    w = list(map(int, input().split()))
    bits = [0] * (10 ** 6 + 100)
    for e in w:
        bits[e] += 1
    cur, res = 0, 0
    for e in bits:
        cur += e
        if cur % 2:
            res += 1
        cur //= 2
    print(res)


def __starting_point():
    main()


__starting_point()
