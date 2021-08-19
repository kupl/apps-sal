def to24hourtime(hour, minute, period):
    hour_str = str(hour)
    minute_str = str(minute)
    if period == 'am':
        if hour <= 9:
            hour_str = '0' + hour_str
        if minute <= 9:
            minute_str = '0' + minute_str
        if hour == 12:
            hour_str = '00'
        return '%s%s' % (hour_str, minute_str)
    else:
        if hour <= 12:
            hour += 12
        if hour == 24:
            hour = 0
        hour_str = str(hour)
        if hour <= 9:
            hour_str = '0' + hour_str
        if minute <= 9:
            minute_str = '0' + minute_str
        if hour == 0:
            hour_str = '12'
        return '%s%s' % (hour_str, minute_str)
