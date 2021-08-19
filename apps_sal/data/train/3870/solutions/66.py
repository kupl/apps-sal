def solve(s):
    indexes = []
    for (n, i) in enumerate(s):
        if i == ' ':
            indexes.append(n)
    res = ''.join(s.split())[::-1]
    for ind in indexes:
        res = res[:ind] + ' ' + res[ind:]
    return res
