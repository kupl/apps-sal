def time_correct(t):
    if not t:
        return t
    r = [int(i) for i in t.split(':') if i.isdigit() and len(i) == 2]
    if len(r) != 3 or t.count(':') != 2:
        return None
    return '{:02}:{:02}:{:02}'.format((r[0] + (r[1] + r[2] // 60) // 60) % 24, (r[1] + r[2] // 60) % 60, r[2] % 60)
