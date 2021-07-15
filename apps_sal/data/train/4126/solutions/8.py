def what_time_is_it(angle):
    hour, minute = divmod(angle, 30)
    hour = int(hour + 12 * (hour == 0))
    minute = int(minute * 2)
    return '{:02d}:{:02d}'.format(hour, minute)
