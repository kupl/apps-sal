def time_correct(t):
    if t == "":
        return ""
    try:
        t = t.split(":")
    except:
        return None
    if len(t) != 3 or not all([i.isdigit() for i in t]):
        return None
    try:
        h, m, s = int(t[0]), int(t[1]), int(t[2])

        m = m + s // 60
        s = s % 60
        h = h + m // 60
        m = m % 60
        h = h % 24

        return str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
    except:
        return None
