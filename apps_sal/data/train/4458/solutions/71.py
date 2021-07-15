import re
def time_correct(t):
    if t == '':
        return t
    if t == None:
        return None
    if re.match('\d\d:\d\d:\d\d$',t):  
        h,m,s = [int(i) for i in t.split(':')]
        if s > 59:
            m += 1
            s -= 60
        if m > 59:
            h += 1
            m -= 60
        while h > 23:
            h -= 24
        return '{:02d}:{:02d}:{:02d}'.format(h,m,s)

