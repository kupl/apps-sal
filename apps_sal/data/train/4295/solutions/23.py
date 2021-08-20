def balanced_num(n):
    return 'Not Balanced' if (lambda r: sum((int(d) for d in r[:(len(r) - 1) // 2])) - sum((int(d) for d in r[len(r) // 2 + 1:])))(str(n)) else 'Balanced'
