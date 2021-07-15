def nth_perm(n, d):
    n -= 1
    _in, out_, f = [], [], []
    for x in range(d):
        f.append(not f or x * f[-1])
        _in.append(str(x))
    for x in range(d):
        i, n = divmod(n, f.pop())
        out_.append(_in.pop(i))
    return ''.join(out_)
