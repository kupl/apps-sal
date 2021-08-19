def array_center(a):
    return [n for n in a if abs(n - sum(a) / len(a)) < min(a)]
