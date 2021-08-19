def what_time_is_it(angle):
    (hh, mm) = divmod(int(2 * angle), 60)
    return '{:02d}:{:02d}'.format(hh if hh else 12, mm)
