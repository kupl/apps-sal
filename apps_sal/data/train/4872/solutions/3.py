def i(s, x, y=0): s.x = getattr(x.x, s._)(y.x)if y else x


class v:
    __init__, compute = i, lambda s: s.x


for p in dir(0):
    value = vars()[p[2:-2]] = type(p, (v,), {"_": p})
