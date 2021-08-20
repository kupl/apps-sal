def or_arrays(x, y, z=0, m=max, l=len):
    return [a | b for (a, b) in zip(x + [z] * (m(l(x), l(y)) - l(x)), y + [z] * (m(l(x), l(y)) - l(y)))]
