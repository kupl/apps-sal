def bus_timer(current_time):
    tim = current_time[3:]
    time = int(tim)
    tume = int(current_time[:2])
    if tume == 5 and time > 55:
            return 60 - time + 15 - 5
    elif tume < 6 and tume >= 0:
        return ((6 - tume) * 60) - 5 - time
        
    else:
        if tume == 23 and time > 55:
            return 360 - 5 + 60 - time
        elif time < 15 and time <= 10:
            return 15 - time - 5
        elif time < 30 and time <= 25:
            return 30 - time - 5
        elif time < 45 and time <=40:
            return 45 - time - 5
        elif time < 15 and time > 10:
            return 30 - time - 5
        elif time < 30 and time > 25:
            return 45 - time - 5
        elif time < 45 and time > 40:
            return 60 - time - 5
        elif time < 60 and time > 55:
            return 75 - time - 5
        else:
            return 60 - time - 5

