def time_correct(t):

    if t == None:
        return None
    elif t == "":
        return ""
    elif len(t) != 8:
        return None
    
    time = t.split(':')
    
    if len(time) != 3:
        return None
    for i in time:
        if i.isdigit() == False:
            return None
    
    sec = [int(time[2]) // 60, int(time[2]) % 60]
    min = [(int(time[1]) + sec[0]) // 60 , (int(time[1]) + sec[0]) % 60]
    hour = [(int(time[0]) + min[0]) % 24]
    
    time = [hour[0], min[1], sec[1]]
    right_time = []
    for time_unit in time:
        if time_unit < 10:
            time_unit = '0' + str(time_unit)
            right_time.append(time_unit)
        else:
            time_unit = str(time_unit)
            right_time.append(time_unit)
    
    result = ':'.join(right_time)
    return result
    

