from datetime import datetime, timedelta

def half_life(person1, person2):
    d1, d2 = (datetime.strptime(p, '%Y-%m-%d') for p in [person1, person2])
    if d1 > d2:
        d1, d2 = d2, d1
    return format(d2 + timedelta((d2 - d1).days), '%Y-%m-%d')
