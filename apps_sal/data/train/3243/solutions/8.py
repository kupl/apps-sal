def bus_timer(current_time):
    (h, m) = list(map(int, current_time.split(':')))
    t = h * 60 + m - 55
    if t < 60 * 5 or t > 23 * 60:
        return (5 + 24 * (h == 23)) * 60 - t
    return min((a - m for a in (10, 25, 40, 55, 70) if a - m >= 0))
