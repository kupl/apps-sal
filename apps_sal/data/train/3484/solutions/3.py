def time_convert(num):
    return "{:02d}:{:02d}".format(*divmod(max(0, num), 60))
