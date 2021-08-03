from functools import reduce


def is_balanced(source, caps):
    _map = {c2: c1 for c1, c2 in zip(caps[0::2], caps[1::2])}
    def red(s, e): return s[:-1] if s and s[-1] == _map.get(e) else s + e
    return not reduce(red, [c for c in source if c in caps], '')
