def balanced_parens(n):
    if n == 0:
        return [""]
    if n == 1:
        return ["()"]
    result = []
    for s in balanced_parens(n - 1):
        result += [s[:i] + "()" + s[i:] for i in range(0, len(s))]
    return list(set(result))
