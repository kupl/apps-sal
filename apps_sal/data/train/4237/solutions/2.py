from datetime import datetime as dt


def to12hourtime(t):
    return dt.strptime(t, '%H%M').strftime('%-I:%M %p').lower()
