from datetime import datetime, timedelta


def day_and_time(mins):
    test_date = datetime(2017, 2, 12) + timedelta(minutes=mins)
    return test_date.strftime("%A %H:%M")
