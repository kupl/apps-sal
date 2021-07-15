def to12hourtime(t):
    hour = int(t[:2])
    
    if hour >= 12:
        hour -= 12
        suf = 'pm'
    else:
        suf = 'am'
    
    if hour == 0:
        hour = 12
    
    return '%s:%s %s' % (hour, t[2:], suf)
