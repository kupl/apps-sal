from datetime import datetime


def get_calendar_week(date_string):
    return int(datetime.strftime(datetime.strptime(date_string, "%Y-%m-%d"), "%V"))
