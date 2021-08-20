def goto(l, b):
    return int(b) - l if b in ('0', '1', '2', '3') and l in (0, 1, 2, 3) else 0
