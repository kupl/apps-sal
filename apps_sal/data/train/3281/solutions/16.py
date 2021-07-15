from datetime import date

def unlucky_days(year):
    count = 0
    for i in range(1, 13):
        if date(year, i, 13).weekday() == 4:
            count += 1
    return count

