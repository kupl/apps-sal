from datetime import date, timedelta


def unlucky_days(year):
    count = 0
    start_day = date(year, 1, 1)
    end_day = date(year, 12, 31)

    while start_day <= end_day:
        if (start_day.weekday() == 4) and (start_day.day == 13):
          #  print(start_day)
            count += 1
        else:
            pass
        start_day += timedelta(days=1)

    return count
