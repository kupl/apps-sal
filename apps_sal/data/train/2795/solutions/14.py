def cockroach_speed(kph):
    mph = kph * 1000
    cph = mph * 100
    cpm = cph / 60
    cps = cpm / 60
    return int(cps)
