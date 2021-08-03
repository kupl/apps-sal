def did_we_win(plays):
    r = 0
    for p in plays:
        if not p:
            continue
        yd, t = p
        if t in ('run', 'pass'):
            r += yd
        elif t == 'sack':
            r -= yd
        elif t == 'turnover':
            return False
        if r > 10:
            return True
    return False
