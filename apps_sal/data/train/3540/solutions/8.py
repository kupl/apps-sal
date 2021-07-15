import datetime
def get_calendar_week(date):
    now = datetime.datetime.strptime(date,'%Y-%m-%d')

    return (datetime.datetime.isocalendar(now)[1])

