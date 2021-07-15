def time_convert(num):
    return "{:02d}:{:02d}".format(*divmod(max(num, 0), 60))
