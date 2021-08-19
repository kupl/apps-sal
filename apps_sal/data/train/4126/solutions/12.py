def what_time_is_it(a):
    return '%02d:%02d' % (int(a / 30) or 12, a % 30 * 2)
