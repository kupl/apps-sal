def balanced_parens(n):
    return list(set([p[:i] + '()' + p[i:] for p in balanced_parens(n - 1) for i in range(0, len(p))])) if n > 1 else ([''], ['()'])[n]
