def growing_plant(u, d, h):
    for i in range(1000):
        if h - u <= 0:
            return i + 1
        h += d - u
