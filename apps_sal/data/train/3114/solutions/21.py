def year_days(y):
    return '%s has %s days' % (y, __import__('calendar').isleap(y) + 365)
