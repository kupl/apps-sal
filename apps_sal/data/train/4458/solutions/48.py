def time_correct(time):
    if not time:
        return time
    try:
        (hours, minutes, seconds) = time.split(':')
    except ValueError:
        return None
    for time in (hours, minutes, seconds):
        if len(time) != 2 or not time.isnumeric():
            return None
    try:
        seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    except ValueError:
        return None
    hours = seconds // 3600
    seconds -= hours * 3600
    hours %= 24
    minutes = seconds // 60
    seconds -= minutes * 60
    final = []
    for time in (hours, minutes, seconds):
        final.append(str(time).zfill(2))
    return ':'.join(final)
