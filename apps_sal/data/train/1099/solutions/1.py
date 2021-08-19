def rating():
    N = int(input())
    a = {}
    ans = 0
    while N:
        N -= 1
        s = input()
        a[s[:-2]] = s[-1:]
    for (k, v) in a.items():
        if v == '+':
            ans += 1
        else:
            ans -= 1
    return ans


def main():
    T = int(input())
    while T:
        T -= 1
        rate = rating()
        print(rate)


def __starting_point():
    main()


__starting_point()
