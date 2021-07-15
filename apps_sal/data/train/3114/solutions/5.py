year_days = lambda y: "{} has {} days".format(y, 365 + (y % 4 == 0) * ((y % 100 != 0) + (y % 400 == 0)) )
