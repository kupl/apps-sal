def what_is_the_time(time_in_mirror):
    hours, minutes = list(map(int, time_in_mirror.split(':')))

    if minutes == 0:
        mirrored_hours = 12 - hours
        mirrored_minutes = 0
    else:
        mirrored_hours = (11 - hours) % 12
        mirrored_minutes = 60 - minutes
    if mirrored_hours == 0:
        mirrored_hours = 12

    return "{:02d}:{:02d}".format(mirrored_hours, mirrored_minutes)
