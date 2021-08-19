def build_a_wall(x=0, y=0):
    if isinstance(x, int) and isinstance(y, int) and (x > 0) and (y > 0):
        if x * y > 10000:
            return "Naah, too much...here's my resignation."
        a = '|'.join(['■■'] * y)
        b = '|'.join(['■'] + ['■■'] * (y - 1) + ['■'])
        if x % 2:
            (a, b) = (b, a)
        return '\n'.join((a if i % 2 else b for i in range(x)))
