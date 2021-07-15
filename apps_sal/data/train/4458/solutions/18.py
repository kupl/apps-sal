def time_correct(t):
    if not t:
        return t
    
    t = t.split(':')
    if len(t) != 3 or not all(len(u) == 2 and u.isdecimal() for u in t):
        return None
        
    hr, min, sec = map(int, t)
    min, sec = min + sec // 60, sec % 60
    hr, min = (hr + min // 60) % 24, min % 60
    return f'{hr:02}:{min:02}:{sec:02}'
