def getTerm(v, first=False):
    a = v[0]
    p = v[1]
    s = ''
    if a != 0:
        if not first:
            s += ' + '
        if p == 0:
            s += str(a)
        else:
            s += str(a) + 'x^' + str(p)
    return s


def main():
    i = 0
    t = int(input())
    while i < t:
        n = int(input())
        v = []
        ans = ''
        for x in range(0, n):
            m = input().split(' ')
            tup = (int(m[0]) * int(m[1]), int(m[1]) - 1)
            v.append(tup)
        v = sorted(v, key=lambda x: (-x[1], x[0]))
        ans = getTerm(v[0], True)
        for j in range(1, n):
            ans += getTerm(v[j])
        print(ans)
        i += 1


def __starting_point():
    main()


__starting_point()
