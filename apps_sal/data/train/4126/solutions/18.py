def what_time_is_it(angle):
    remain = int((angle - angle // 30 * 30) / 30 * 60)
    hour = int(angle / 30) if angle >= 30 else 12
    return '{:02d}'.format(hour) + ':' + '{:02d}'.format(remain) if remain else '{:02d}'.format(hour) + ':00'
