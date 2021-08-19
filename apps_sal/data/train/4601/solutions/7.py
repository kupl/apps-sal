def mormons(a, r, t, m=0):
    return m if a >= t else mormons(a * (r + 1), r, t, m + 1)
