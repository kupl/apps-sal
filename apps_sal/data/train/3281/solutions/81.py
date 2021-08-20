from datetime import datetime


def unlucky_days(year):
    """returns the numbers of Fridays 13th found in a given year.

       example:
       >> print('%s unlucky days found in year 2020.' % unlucky_days(2020))
    """
    spooky_days = 0
    if isinstance(year, int) and 0 < year < 10000:
        months = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
        for m in months:
            date_to_check = str(year) + '-' + m + '-13'
            day = datetime.strptime(date_to_check, '%Y-%m-%d').weekday()
            if day == 4:
                spooky_days += 1
    return spooky_days
