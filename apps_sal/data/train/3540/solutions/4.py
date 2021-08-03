from datetime import datetime


def get_calendar_week(date):
    return datetime.strptime(date, '%Y-%m-%d').isocalendar()[1]
