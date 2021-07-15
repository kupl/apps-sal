year_days = lambda y: "{} has {} days".format(y, __import__('calendar').isleap(y) + 365)

