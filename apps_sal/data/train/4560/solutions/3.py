def answer(s, a):
    s = set(s.lower().split())
    a = [(x, set(x.lower().split())) for x in a]
    r = max(a, key=lambda x: len(x[1] & s))
    if r[1] & s:
        return r[0]
