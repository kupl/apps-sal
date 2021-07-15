def time_convert(num):
    return '{:02}:{:02}'.format(*divmod(max(0, num), 60))
