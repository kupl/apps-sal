import datetime
def day(date):
    return datetime.datetime.strptime(date, '%Y%m%d').strftime('%A')
