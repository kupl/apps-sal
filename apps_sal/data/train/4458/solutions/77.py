def time_correct(t):
    if t is None: return None
    if t == '': return ''
    if len(t) != 8: return None
    t = t.split(':')
    if len(t) != 3 or sum(1 for v in t if not v.isdigit()) != 0: return None
    t = [int(a) for a in t]
    s = (t[0] * 3600 + t[1] * 60 + t[2]) % (3600 * 24)
    return "%02d:%02d:%02d" % (s // 3600, s % 3600 // 60, s % 60)
