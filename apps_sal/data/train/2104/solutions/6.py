def main():
    n = int(input())
    l = sorted(map(int, input().split()))
    r = (l[n - 1] - l[0]) * (l[-1] - l[n])
    if r:
        r = min(r, min(b - a for a, b in zip(l[1:n], l[n:-1])) * (l[-1] - l[0]))
    print(r)


def __starting_point():
    main()


__starting_point()
