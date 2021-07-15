def what_time_is_it(angle):
    if angle % 360 == 0:
        return '12:00'
    m = int(angle % 360 / 360 * 720)
    return '{}:{}'.format(str(m//60).zfill(2) if m//60 > 0 else '12', str(m%60).zfill(2))
