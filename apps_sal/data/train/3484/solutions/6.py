def time_convert(num):
    if num <= 0:
        return '00:00'
    
    if num < 60:
        if num <= 9:
            num_str = '0' + str(num)
        else:
            num_str = str(num)
        return '00:' + num_str
    
    hour = int(num / 60)
    hour_str = str(hour)
    minute = num - hour * 60
    minute_str = str(minute)

    if hour <= 9:
        hour_str = '0' + hour_str
    if minute <= 9:
        minute_str = '0' + minute_str
    
    return '%s:%s' % (hour_str, minute_str)
