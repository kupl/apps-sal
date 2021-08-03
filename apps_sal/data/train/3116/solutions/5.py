def cal_n_bug(h, l, w):
    lst = [l // 2 - 3 * h, 8 * h - l - w, w - 4 * h + l // 2]
    return lst if lst[0] >= 0 and lst[1] >= 0 and lst[2] >= 0 else [-1, -1, -1]
