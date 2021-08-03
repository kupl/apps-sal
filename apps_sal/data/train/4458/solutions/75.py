from re import match


def pad(n):
    return "0" + str(n) if n < 10 else str(n)


def time_correct(t):
    if not t:
        return t
    if not match('\d{2}:\d{2}:\d{2}', t):
        return None
    h, m, s = map(int, t.split(":"))
    secs = (h * 3600 + m * 60 + s) % (24 * 3600)
    h, m, s = secs // 3600, (secs % 3600) // 60, secs % 60
    return ":".join(map(pad, [h, m, s]))
