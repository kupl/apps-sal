import datetime
get_calendar_week=lambda d:datetime.date(*map(int,d.split('-'))).isocalendar()[1]
