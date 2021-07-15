from datetime import datetime


def get_calendar_week(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").isocalendar()[1]    
