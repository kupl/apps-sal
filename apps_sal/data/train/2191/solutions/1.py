def main():
    input()
    aa = sorted(map(int, input().split()))
    maxa = aa[-1]
    m = [False] * (maxa + 1)
    x = []
    b = res = 0
    for a in aa:
        if b != a:
            m[a] = True
            for i in range(b, a):
                x.append(b)
            b = a
    x.append(b)
    for a in range(maxa - 1, 1, -1):
        if a < res:
            break
        if m[a]:
            for b in range(2 * a - 1, maxa + 2 * a, a):
                res = max(res, x[min(b, maxa)] % a)
    print(res)


def __starting_point():
    main()
__starting_point()
