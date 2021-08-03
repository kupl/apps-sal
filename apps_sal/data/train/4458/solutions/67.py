def time_correct(t):
    if t == "":
        return t

    if not t or ":" not in t or len(t.split(":")) != 3 or any(c.isalpha() for c in t) or any(not c.isdigit() and c != ":" for c in t):
        return None

    h, m, s = (int(i) for i in t.split(":"))

    if s > 59:
        m += 1
        s -= 60

    if m > 59:
        h += 1
        m -= 60

    while h > 23:
        h -= 24

    return ":".join([str(h).rjust(2, "0"), str(m).rjust(2, "0"), str(s).rjust(2, "0")])
