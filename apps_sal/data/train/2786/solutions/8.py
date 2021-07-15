from calendar import day_name, monthcalendar

def day(date):
    year, month, day = list(map(int, (date[:4], date[4:6], date[6:])))
    first_day = monthcalendar(year, month)[0].index(1)
    return day_name[ (first_day+day-1) % 7 ]

