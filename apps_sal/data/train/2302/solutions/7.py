def solve(n, d, da, q, qa):
    a = [d]
    x = d
    for di in da:
        x = min(x, max(x - di, di - x))
        a.append(x)
    b = [1]
    x = 1
    for i in range(n - 1, -1, -1):
        di = da[i]
        if di // 2 < x:
            x += di
        b.append(x)
    b.reverse()
    for qi in qa:
        if b[qi] <= a[qi - 1]:
            print('YES')
        else:
            print('NO')


def main():
    (n, d) = input().split()
    n = int(n)
    d = int(d)
    da = list(map(int, input().split()))
    q = input()
    q = int(q)
    qa = list(map(int, input().split()))
    solve(n, d, da, q, qa)


def __starting_point():
    main()


__starting_point()
