def build_a_wall(x=None, y=None):
    try:
        if x * y > 10000:
            return "Naah, too much...here's my resignation."
        if x * y <= 0:
            raise Exception
        d = ['|'.join(['■■'] * y), '|'.join(['■'] + ['■■'] * (y - 1) + ['■'])]
        r = []
        for i in range(x):
            r.append(d[i % 2])
        return '\n'.join(r[::-1])

    except:
        return
