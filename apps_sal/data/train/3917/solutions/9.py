def freeway_game(dist, speed, cars):
    res, exit = 0, dist / speed
    def check(t, s1, s2): return s * t < exit * s2 * 60

    for t, s in cars:
        if t < 0 and speed > s:
            res += check(-t, s, speed - s)
        elif t > 0 and speed < s:
            res -= check(t, s, s - speed)
    return res
