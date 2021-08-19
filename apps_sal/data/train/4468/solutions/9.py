def simplify(n):
    return '+'.join([f'{x}*{10 ** i}' if i else x for (i, x) in enumerate(str(n)[::-1]) if x != '0'][::-1])
