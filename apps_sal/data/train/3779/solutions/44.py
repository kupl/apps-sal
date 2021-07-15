def past(hours, minutes, seconds):
    hours = (hours * 3600) * 1000
    minutes = (minutes * 60) * 1000
    seconds = seconds * 1000
    return hours + minutes + seconds
