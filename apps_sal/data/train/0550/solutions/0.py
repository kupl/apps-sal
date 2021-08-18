
def main():
    t = int(input())
    while (t):
        m, n = map(int, input().split())
        a, b = bin(m)[2:], bin(n)[2:]
        max = m ^ n
        if len(a) > len(b):
            diff = len(a) - len(b)
            b = ("0" * diff) + b
        elif len(a) < len(b):
            diff = len(b) - len(a)
            a = ("0" * diff) + a
        ll = len(b)
        count = 0
        for i in range(ll - 1):
            s = b[ll - 1] + b
            s = s[:ll]

            tt = m ^ int(s, 2)
            if tt > max:
                max = tt
                count = i + 1
            b = s

        print(count, max)
        t -= 1


def __starting_point():
    main()


__starting_point()
