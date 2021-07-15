from datetime import datetime

def to24hourtime(h, m, p):
    t = f'{h}:{m} {p}'
    return datetime.strptime(t, '%I:%M %p').strftime('%H%M')
