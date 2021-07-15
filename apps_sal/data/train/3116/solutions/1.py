def cal_n_bug(n_head, n_leg, n_wing):
    s = (n_leg - 6 * n_head) / 2
    b = 8 * n_head - n_wing - n_leg
    d = s + n_wing - n_head
    return [s, b, d] if s >= 0 and b >= 0 and d >= 0 else [-1, -1, -1]
