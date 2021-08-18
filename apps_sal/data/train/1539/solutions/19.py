

def toint(s): return int(s)
def tofloat(s): return float(s)


def get_int():
    s = input()
    return int(s)


def main():
    t = get_int()
    while t:
        j = input()
        s = input()

        a = [0] * 256
        for i in j:
            a[ord(i)] = 1
        res = 0
        for i in s:
            res += a[ord(i)]
        print(res)
        t -= 1
    pass


def __starting_point():
    main()


__starting_point()
