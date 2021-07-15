def cockroach_speed(kph):
    # 1000 m in km
    mph = kph * 1000
    # 100 cm in m
    cph = mph * 100
    # 60 min in hour
    cpm = cph / 60
    # 60 sec in min
    cps = cpm / 60
    return int(cps)

# I'm just tired of oneliners =)

