def what_time_is_it(n):
    from math import floor
    temp = n * 2
    hours = str(floor(temp / 60))
    minutes = str(floor(temp % 60))
    if temp // 60 == 0:
        hours = '12'
    if len(hours) == 1:
        hours = '0' + hours
    if len(minutes) == 1:
        minutes = '0' + minutes
    return hours + ':' + minutes
