def year_days(y): return '%d has %d days' % (y, 365 + (y % 400 < 1 or y % 100 and y % 4 < 1))
