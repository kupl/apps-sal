from datetime import datetime


def get_calendar_week(date_string: str):
    return datetime.strptime(date_string, '%Y-%m-%d').isocalendar()[1]
