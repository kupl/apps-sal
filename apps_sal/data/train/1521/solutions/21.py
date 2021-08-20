def ipnl(n):
    return [int(input()) for _ in range(n)]


def inp():
    return int(input())


def ip():
    return [int(w) for w in input().split()]


for _ in range(inp()):
    n = inp()
    tot = [0] * (n + 1)
    sco = [0] * n
    x = [ip() + [i] for i in range(n)]
    x.sort(key=lambda i: i[0])
    for i in range(n - 1):
        (l, r, i1) = (x[i][0], x[i][1], x[i][2])
        for j in reversed(list(range(i + 1, n))):
            (nl, nr, j1) = (x[j][0], x[j][1], x[j][2])
            if nl > l:
                if nr <= r:
                    sco[i1] += 2
                else:
                    sco[i1] += 1
                    sco[j1] += 1
            elif nl == l:
                if nr > r:
                    sco[j1] += 2
                elif nr == r:
                    sco[i1] += 1
                    sco[j1] += 1
                else:
                    break
        if j > i + 1:
            sco[i1] += 2 * (j - i)
    print(*sco)
