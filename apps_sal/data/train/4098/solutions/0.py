def new_numeral_system(n):
    a = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if c <= n]
    return ['{} + {}'.format(a[i], a[-1 - i]) for i in range((len(a) + 1) // 2)]
