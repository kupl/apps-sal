from datetime import datetime
import calendar
def day(date):
    return calendar.day_name[datetime.strptime(date,"%Y%m%d").weekday()]
