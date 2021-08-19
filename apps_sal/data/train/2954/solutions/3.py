def riders(stations):
    (c, acc) = (0, 0)
    for d in stations:
        c += acc + d > 100
        acc = d if acc + d > 100 else acc + d
    return c + bool(acc)
