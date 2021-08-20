import datetime


def unlucky_days(year):
    dates_13 = [datetime.datetime.strptime(f'{year}-{i}-13', '%Y-%m-%d').date() for i in range(1, 13)]
    res = [mon for mon in dates_13 if mon.isoweekday() == 5]
    return len(res)
