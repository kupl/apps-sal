def get_military_time(time):
    if time[-2:] == 'AM':
        hour = '00' if time[0:2] == '12' else time[0:2]
    else:
        hour = '12' if time[0:2] == '12' else str(int(time[0:2]) + 12)
    return hour + time[2:-2]
