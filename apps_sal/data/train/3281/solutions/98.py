from datetime import datetime


def unlucky_days(year):
    days = 0
    date_string = "13/{}/{}"
    for i in range(1, 13):
        date_obj = datetime.strptime(date_string.format(str(i).zfill(2), str(year)), '%d/%m/%Y').weekday()
        if date_obj == 4:
            days += 1
    return days
