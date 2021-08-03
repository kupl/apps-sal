def is_triangle(a, b, c):
    if (a or b or c) < 0:
        return False
    v = list()
    v.append(a)
    v.append(b)
    v.append(c)
    v.sort()
    _a = v.pop()
    _b = v.pop()
    _c = v.pop()

    if _a < _b + _c:
        return True
    if _a == _b + _c:
        return False
    return False
