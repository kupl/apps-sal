def what_time_is_it(angle):
    hr = int(angle // 30)
    mn = int((angle % 30) * 2)
    if hr == 0:
        hr = 12
    return '{:02d}:{:02d}'.format(hr, mn)
