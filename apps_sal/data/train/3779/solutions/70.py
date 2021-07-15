def past(hours, minutes, sec):
    if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= sec <= 59:
        return (hours * 60 * 60 + minutes * 60 + sec) * 1000
    else:
        return 0
