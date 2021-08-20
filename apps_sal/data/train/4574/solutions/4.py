def build_a_wall(x=None, y=None):
    if isinstance(x, int) and isinstance(y, int) and (x > 0) and (y > 0):
        if x * y > 10000:
            return "Naah, too much...here's my resignation."
        hb = '■'
        b = hb + hb
        even = ((b + '|') * y)[:-1]
        odd = hb + '|' + (b + '|') * (y - 1) + hb
        return '\n'.join([even if r % 2 == 0 else odd for r in range(x - 1, -1, -1)])
    return None
