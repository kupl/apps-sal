vn = [(-1, 0), (0, -1), (0, 1), (1, 0)]
mr = vn + [(-1, -1), (-1, 1), (1, -1), (1, 1)]


def get_neighbourhood(nh, a, p):
    h, w, nh, x, y = list(range(len(a))), list(range(len(a[0] if a else []))), mr if "r" in nh else vn, *p
    return [a[x + i][y + j] for i, j in nh if ((x + i) in h and (y + j) in w)] if x in h and y in w else []
