import re
def time_correct(t):
    if t == '':
        return ''
    if t and re.search(r'[0-9]{2}:[0-9]{2}:[0-9]{2}', t):
        sec = int(t[-2:])
        min = int(t[3:5])
        hr = int(t[:2])
        if sec > 59:
            sec -= 60
            min += 1
        if min > 59:
            min -= 60
            hr += 1
        if hr > 23:
            hr -= hr//24*24
        return '{:02d}:{:02d}:{:02d}'.format(hr, min, sec)
    return None
