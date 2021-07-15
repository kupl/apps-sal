def freeway_game(km, kph, cars):
    t = km / kph
    c = 0
    for dt, speed in cars:
        d = km - (t - dt/60) * speed
        if dt <= 0:
            c += d > 0
        else:
            c -= d < 0
    return c
