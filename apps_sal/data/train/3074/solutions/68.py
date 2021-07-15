def growing_plant(u, d, h):
    p = 0
    count = 1
    while h > p:
        p += u
        if h <= p:
            break
        p -= d
        count += 1
    return count
