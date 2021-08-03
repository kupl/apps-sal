def what_time_is_it(angle):
    hour = str(int((angle // 30) or 12)).zfill(2)
    min = str(int(2 * (angle % 30))).zfill(2)
    return f'{hour}:{min}'
