def balanced_parens(n):
    return list(dfs([], 0, 0, n))


def dfs(s, open, close, maxP):
    if close == maxP:
        yield ''.join(s)
        return
    if open > close:
        s.append(')')
        yield from dfs(s, open, close + 1, maxP)
        s.pop()
    if open < maxP:
        s.append('(')
        yield from dfs(s, open + 1, close, maxP)
        s.pop()
