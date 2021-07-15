def cube_odd(a):
    return sum(e**3 for e in a if e % 2) if all(type(e) == int for e in a) else None
