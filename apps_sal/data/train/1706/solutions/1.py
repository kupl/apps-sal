def rectangle_rotation(a, b):
    wid_even = 2 * int(a / 2 / 2 ** 0.5) + 1
    hei_even = 2 * int(b / 2 / 2 ** 0.5) + 1
    wid_odd = 2 * int(a / 2 / 2 ** 0.5 + 1 / 2)
    hei_odd = 2 * int(b / 2 / 2 ** 0.5 + 1 / 2)
    return wid_even * hei_even + wid_odd * hei_odd
