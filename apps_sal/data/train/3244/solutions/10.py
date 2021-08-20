d = __import__('collections').OrderedDict([(int(y), float(x)) for (x, y) in __import__('re').findall('(\\d\\.\\d{2}).*?(\\d+)', '\n        $3.85 for 40 newspapers\n        $1.93 for 20\n        $0.97 for 10\n        $0.49 for 5\n        $0.10 for 1\n        ')])


def cheapest_quote(n, r=0):
    for (k, v) in d.items():
        r += n // k * v
        n %= k
        if not n:
            break
    return round(r, 2)
