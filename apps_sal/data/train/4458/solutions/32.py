def time_correct(t):
    if t == "":
        return ""
    if not t:
        return None
    if len(t.split(":")) != 3:
        return None
    h, m, s = t.split(":")
    if not h.isdigit() or not m.isdigit() or not s.isdigit():
        return None
    if len(h) != 2 or len(m) != 2 or len(s) != 2:
        return None
    sec = int(s) % 60
    min = (int(m) + int(s) // 60) % 60
    hour = (int(h) + (int(m) + int(s) // 60) // 60) % 24
    return "{:02}:{:02}:{:02}".format(hour, min, sec)
