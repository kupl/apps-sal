from datetime import datetime


def to12hourtime(time):
    return datetime.strptime(time, '%H%M').strftime('%I:%M %p').lstrip('0').lower()
