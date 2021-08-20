import datetime


def get_calendar_week(d):
    return datetime.date(*map(int, d.split('-'))).isocalendar()[1]
