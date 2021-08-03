def time_correct(t):
    if not t:
        return t
    try:
        h, m, s = t.split(':')
        h, m, s = int(h), int(m), int(s)
    except ValueError:
        return None
    m += s // 60
    s %= 60
    h += m // 60
    m %= 60
    h %= 24
    def fill(n): return str(n).zfill(2)
    return '{}:{}:{}'.format(fill(h), fill(m), fill(s))
