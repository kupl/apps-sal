def freeway_game(d, speed, arr):
    t = d / speed * 60
    print(t)
    c = 0

    for data in arr:
        if data[0] < 0:
            if d / data[1] * 60 > t - data[0]:
                c += 1
        if data[0] > 0:
            if d / data[1] * 60 < t - data[0]:
                c -= 1

    return c
