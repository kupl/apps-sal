def year_days(y): return "{} has {} days".format(y, __import__('calendar').isleap(y) + 365)
