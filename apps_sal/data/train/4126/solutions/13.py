def what_time_is_it(angle):
    return str(int(angle / 30) or 12).zfill(2) + ':' + str(int(angle % 30 * 2)).zfill(2)
