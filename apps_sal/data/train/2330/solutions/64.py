def Tree():
    S = input()
    N = len(S)

    if S[0] == "0" or S[-1] == "1":
        return []

    for i in range(N - 1):
        if S[i] != S[N - i - 2]:
            return []

    res = []
    path = S.count("1")
    for i in range(1, path + 1):
        res.append((i, i + 1))

    u = len(res) + 1
    v = 1
    for s in S[:-1]:
        if s == "1":
            v += 1
        else:
            u += 1
            res.append((v, u))

    return res


def __starting_point():
    tree = Tree()
    if tree:
        for x, y in tree:
            print(x, y)
    else:
        print(-1)
__starting_point()
