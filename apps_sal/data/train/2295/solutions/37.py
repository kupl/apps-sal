def slv(n, ab):
    if [a for a, b in ab] == [b for a, b in ab]:
        return 0
    c = []
    W = 0
    ret = 0
    for i, (a, b) in enumerate(ab):
        if a - b > 0:
            c.append([b, a - b])
        else:
            ret += b
            W += b - a
    W -= 1
    c.sort(key=lambda x: x[0])
    ret += sum([v for v, w in c[1:]])
    return ret


n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
print((slv(n, ab)))
