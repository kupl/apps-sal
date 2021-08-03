import calendar


def unlucky_days(year):
    c = calendar.Calendar()
    counter = 0
    for month in range(1, 13):
        print(f"Months is {month}")
        for day in c.itermonthdays2(year, month):
            print(f"Day is {day}")
            if day[0] == 13 and day[1] == 4:
                print(f"This is Friday 13th {day}")
                counter += 1
    return counter
