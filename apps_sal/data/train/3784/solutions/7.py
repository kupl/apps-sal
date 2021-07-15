def sort_transform(a):
    a = [chr(e) for e in a]
    r = sorted(a)
    x = ''.join(r[:2] + r[-2:])
    return '-'.join([''.join(a[:2]+a[-2:]), x, x[::-1], x])
