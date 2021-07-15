from datetime import datetime
def day(date):
    return '{:%A}'.format(datetime.strptime(date, '%Y%m%d'))
