def split_exp(n):
    try:
        dot = n.index('.')
    except:
        dot = len(n)
    return [n[i] + '0' * (dot - 1 - i) for i in range(dot) if n[i] != '0'] +\
        ['.' + '0' * (i - dot - 1) + n[i] for i in range(dot + 1, len(n)) if n[i] != '0']
