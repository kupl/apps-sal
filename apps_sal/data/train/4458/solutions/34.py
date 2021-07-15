from re import match

is_valid = lambda s: isinstance(s, str) and bool(match(r'^\d\d:\d\d:\d\d$', s))

def time_correct(sd):
    if sd == '': return sd
    if is_valid(sd):
        h, m, s = list(map(int, sd.split(':')))
        q, r = divmod(s, 60)
        m, s = m + q, r
        q, r = divmod(m, 60)
        h, m = (h + q) % 24, r
        return f'{h:02}:{m:02}:{s:02}'
