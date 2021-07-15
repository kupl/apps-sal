def or_arrays(a, b, filler=0):
    al, bl = len(a), len(b)
    return list([v[0] | v[1] for v in zip(a + [filler] * (max(al, bl) - al), b + [filler] * (max(al, bl) - bl))])

