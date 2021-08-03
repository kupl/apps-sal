def to12hourtime(time_string):
    hour_str = time_string[0] + time_string[1]
    minute_str = time_string[2] + time_string[3]

    if int(hour_str) < 12:
        if int(hour_str) == 0:
            hour_str = 12
        return '%s:%s am' % (int(hour_str), minute_str)
    else:
        hour = int(hour_str) - 12
        if hour == 0:
            hour = 12
        return '%s:%s pm' % (hour, minute_str)
