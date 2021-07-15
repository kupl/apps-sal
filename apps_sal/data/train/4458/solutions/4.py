def time_correct(t):
    try:
        h, m, s = (int(n) for n in t.split(":") if len(n) == 2)
    except (AttributeError, ValueError):
        return "" if t == "" else None
    s, m = s % 60, m + s // 60
    m, h = m % 60, (h + m // 60) % 24
    return f"{h:02d}:{m:02d}:{s:02d}"
