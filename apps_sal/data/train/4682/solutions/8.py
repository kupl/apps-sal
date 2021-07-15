import datetime
def date_correct(date):
    print(date)
    if date is None or date is '':
        return date
    try:
        day, month, year = date.split('.')
        if len(day) is not 2 or len(month) is not 2:
            return None
        day = int(day)
        month = int(month)
        year = int(year)
    except:
        return None
    extra_years = month // 12
    if month >= 12 and month % 12 == 0:
        extra_years -=1
    year = year + extra_years
    correct_months = month % 12
    if correct_months == 0:
        correct_months = 12
    print(date, year, correct_months)
    result = datetime.datetime(year=year, month=correct_months, day=1)
    result += datetime.timedelta(days=day-1)
    print(result)
    return '.'.join([str(value).zfill(2) for value in [result.day, result.month, result.year] ])
