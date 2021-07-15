import datetime

def unlucky_days(year):
    number = 0
    for month in range(1, 13):
        d = datetime.date(year, month, 13)
        if (d.strftime("%A") == "Friday"):
            number += 1
    return number
