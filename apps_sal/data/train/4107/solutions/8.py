from datetime import datetime

def half_life(person1, person2):
    d1, d2 = map(lambda s: datetime.strptime(s, '%Y-%m-%d'), sorted((person1, person2)))
    return datetime.strftime(d2 + (d2 - d1), '%Y-%m-%d')
