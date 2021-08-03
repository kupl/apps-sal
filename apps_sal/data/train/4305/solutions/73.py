def order_weight(strng):
    cs = strng.strip().split()
    ls = sorted(sorted(cs), key=cc)
    return ' '.join(ls)


def cc(a):
    return sum(map(int, a))
