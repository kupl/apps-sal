def to24hourtime(hour, minute, period):
    if hour < 10:
        hour = '0' + str(hour)
    else:
        hour = str(hour)

    if minute < 10:
        minute = '0' + str(minute)
    else:
        minute = str(minute)

    time = hour + minute
    if period == 'pm' and int(hour) != 12:
        time = str(int(time) + 1200)

    if period == 'am' and int(hour) == 12:
        time = str(int(time) - 1200)
        if int(minute) < 10:
            time = '000' + time
        else:
            time = '00' + time

    print((hour, minute, period))
    return time
