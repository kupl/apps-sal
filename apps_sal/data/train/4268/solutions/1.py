def next_num(n):

    def dfs(m=0, i=0, fromZ=0):
        if m > n:
            yield m
        elif i < len(s):
            m *= 10
            for d in range(0 if fromZ else s[i], 10):
                if not (m + d) % (i + 1):
                    yield from dfs(m + d, i + 1, fromZ or d > s[i])
    s = list(map(int, str(n)))
    ret = next(dfs(), None)
    if ret is None:
        s = [1] + [0] * len(s)
        ret = next(dfs(), None)
    return ret
