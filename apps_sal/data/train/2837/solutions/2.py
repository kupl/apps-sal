def what_is_the_time(time_in_mirror):
    CW_HRS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    MIRROR = [0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11]
    if time_in_mirror in ['12:00', '12:30', '06:00', '06:30']:
        return time_in_mirror
    (hours, minutes) = time_in_mirror.split(':')
    (hours, minutes) = (int(hours), int(minutes))
    hrs = abs(12 - hours) if minutes == 0 else MIRROR[hours]
    mins = 0 if minutes == 0 else 60 - minutes
    return '{:02}:{:02}'.format(hrs, mins)
