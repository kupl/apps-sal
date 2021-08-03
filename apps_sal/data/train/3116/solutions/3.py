
def cal_n_bug(n_head, n_leg, n_wing):
    n_s = (n_leg - 6 * n_head) / 2
    n_d = (n_leg - 8 * n_head + 2 * n_wing) / 2
    n_b = (-n_leg + 8 * n_head - n_wing)
    if n_s > -1 and n_d > -1 and n_b > -1:
        return [n_s, n_b, n_d]
    else:
        return [-1, -1, -1]
