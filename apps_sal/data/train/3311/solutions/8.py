def reverse_invert(lst):
    return [(-1) ** (v > 0) * int(str(abs(v))[::-1]) for v in lst if isinstance(v, int)]
