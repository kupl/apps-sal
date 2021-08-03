def time_correct(t):
    if t == "":
        return ""
    if not t or "+" in t:
        return None
    try:
        h, m, s = map(int, t.split(':'))
    except:
        return None
    m += s // 60
    s = s % 60
    h += m // 60
    m = m % 60
    h = h % 24
    return f'{h:02}:{m:02}:{s:02}'
