from datetime import date

unlucky_days = lambda year: sum(date(year, month, 13).weekday() == 4 for month in range(1, 13))
