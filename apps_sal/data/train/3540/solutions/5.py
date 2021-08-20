def isLeap(y):
    return y % 400 == 0 or (y % 100 != 0 and y % 4 == 0)


def numDays(y, m, d):
    return sum([31, 29 if isLeap(y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:m - 1]) + d


def whatDay_Jan1st(y):
    y = (y - 1) % 400
    return (y // 100 * (76 * 1 + 24 * 2) + y % 100 // 4 * (1 + 1 + 1 + 2) + y % 4) % 7 + 1


def get_calendar_week(date_string):
    (y, m, d) = map(int, date_string.split('-'))
    if m == 12 and d in [29, 30, 31]:
        s = whatDay_Jan1st(y + 1)
        if s == 4 or (s == 3 and d in [30, 31]) or (s == 2 and d == 31):
            return 1
    s = whatDay_Jan1st(y)
    if m == 1 and (s == 5 and d in [1, 2, 3] or (s == 6 and d in [1, 2]) or (s == 7 and d == 1)):
        (y, m, d) = (y - 1, 12, 28)
        s = whatDay_Jan1st(y)
    dateW01_1 = [1, 0, -1, -2, 4, 3, 2][s - 1]
    return (numDays(y, m, d) - dateW01_1) // 7 + 1
