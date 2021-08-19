def to12hourtime(timestring):
    print(timestring)
    hour = int(timestring[:2])
    mins = timestring[2:]
    if hour >= 12:
        noon = 'pm'
        hour -= 12
    else:
        noon = 'am'
    if hour == 0:
        hour = 12
    return '{}:{} {}'.format(hour, mins, noon)
