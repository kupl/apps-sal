from datetime import date


def get_calendar_week(s):
    return date(*map(int, s.split("-"))).isocalendar()[1]
