import calendar
cal = calendar.Calendar()


def unlucky_days(input):
    count = 0
    for month in range(1, 13):
        results = cal.monthdays2calendar(input, month)
        for result in results:
            if (13, 4) in result:
                count += 1
    return count
