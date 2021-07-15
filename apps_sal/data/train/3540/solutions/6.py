from datetime import datetime

def get_calendar_week(date_string):
    d = datetime.strptime(date_string, '%Y-%m-%d')
    return d.isocalendar()[1]
