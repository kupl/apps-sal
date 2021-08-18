def cal_n_bug(head, leg, wing):
    x = leg / 2 - head * 3
    head -= x
    y = head * 2 - wing
    z = head - y
    if all(n >= 0 for n in (x, y, z)):
        return [x, y, z]
    return [-1, -1, -1]
