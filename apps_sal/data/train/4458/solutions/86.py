import re


def time_correct(time):
    if time == None:
        return None
    elif time == '':
        return ''
    pattern = re.compile('[0-9][0-9]:[0-9][0-9]:[0-9][0-9]')
    if pattern.match(time):
        t = time.split(':')
        hours = int(t[0])
        minutes = int(t[1])
        seconds = int(t[2])
        while seconds >= 60:
            seconds -= 60
            minutes += 1
        while minutes >= 60:
            minutes -= 60
            hours += 1
        while hours >= 24:
            hours -= 24
        return str('{:02d}'.format(hours)) + ':' + str('{:02d}'.format(minutes)) + ':' + str('{:02d}'.format(seconds))
