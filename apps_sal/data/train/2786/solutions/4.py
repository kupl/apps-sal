from dateutil import parser
import calendar
def day(date):
    return calendar.day_name[parser.parse(date).weekday()]

