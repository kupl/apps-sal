from calendar import Calendar, MONDAY, FRIDAY

def unlucky_days(year):
    c = Calendar(firstweekday=MONDAY)
    return sum(1 for x in [[1 for d, wd in c.itermonthdays2(year, m) if wd == FRIDAY and d == 13] for m in range(1,13)] if x)

