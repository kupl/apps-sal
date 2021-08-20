def split_exp(n):
    d = n.split('.')
    result = [c + '0' * (len(d[0]) - i - 1) for (i, c) in enumerate(d[0]) if c != '0']
    if len(d) == 2:
        result += ['.' + '0' * i + c for (i, c) in enumerate(d[1]) if c != '0']
    return result
