def solve(d):
    op = []
    p = (10**5) - 2
    if(d > 0):
        while d > 0:
            p = min(d, p)
            op.append(p + 1)
            op.append(p + 2)
            op.append(1)
            d = d - p
    else:
        op.append(1)
    print(len(op))
    print(*op)


t = int(input())
for i in range(t):
    d = int(input())
    solve(d)
