def prod2sum(a, b, c, d):
    result = map(sorted, [map(abs, [a * d - b * c, a * c + b * d]), map(abs, [b * d - a * c, b * c + a * d])])
    return sorted(result, key=lambda x: x[0])[:2 - (a == b or b == 0)]
