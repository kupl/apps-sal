from datetime import date


def get_calendar_week(date_string):
    return date.isocalendar(date(*map(int, date_string.split('-'))))[1]
