def solve(d):
    op = []
    p = (10**5) - 2
    if d > 0:
        while d > 0:
            p = min(d, p)
            op.append(p + 1)
            op.append(p + 2)
            op.append(1)
            d = d - p
    else:
        op.append(d + 1)
        op.append(d + 2)
    print(len(op))
    print(*op)


def __starting_point():
    for test in range(int(input())):
        d = int(input())
        solve(d)


__starting_point()
