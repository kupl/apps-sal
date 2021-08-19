def to24hourtime(hour, minute, period):
    if 'pm' in period:
        time = str(int(hour + 12)) + str(minute).zfill(2)
        if hour == 12:
            return '12' + str(minute).zfill(2)
        return time
    else:
        time = str(str(hour).zfill(2)) + str(minute).zfill(2)
        if hour == 12:
            return '00' + str(minute).zfill(2)
        return time
