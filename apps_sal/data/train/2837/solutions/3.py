def what_is_the_time(time_in_mirror):
    l = []
    hour = []
    minute = []
    res = []
    for i in time_in_mirror:
        l.append(i)
    l.pop(2)
    hour.append(l[0])
    hour.append(l[1])
    minute.append(l[2])
    minute.append(l[3])
    hour = ''.join(hour)
    minute = ''.join(minute)
    hour = int(hour)

    minute = int(minute)
    if(hour < 11 and minute != 0):
        hour = 11 - hour
    elif(hour < 11 and minute == 0):
        hour = 12 - hour
    elif(hour == 11 and minute != 0):
        hour = 12
    elif(hour == 11 and minute == 0):
        hour = 1
    elif(hour == 12 and minute != 0):
        hour = 11
    elif(hour == 12 and minute == 0):
        hour = 12
    if minute == 0:
        minute = 0
    else:
        minute = 60 - minute
    if(hour < 10):
        res.append(str(0))
        res.append(str(hour))
    else:
        res.append(str(hour))
    res.append(':')
    if(minute < 10):
        res.append('0')
        res.append(str(minute))
    else:
        res.append(str(minute))
    res = ''.join(res)
    return res
