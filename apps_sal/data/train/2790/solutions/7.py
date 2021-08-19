def f(s):
    return ''.join((s[i] for i in range(len(s) - 1) if s[i] != s[i + 1])) + s[-1]


def dup(arry):
    return [f(s) for s in arry]
