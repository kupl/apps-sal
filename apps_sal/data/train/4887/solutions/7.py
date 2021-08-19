def days(date, month, year):

    def leap_year(y):
        if y % 4 == 0:
            if y > 1752 and y % 100 == 0:
                if y % 400 == 0:
                    return True
                else:
                    return False
            return True

    def days_in_years(y):
        n = 0
        for num in range(1, y):
            if leap_year(num):
                n += 1
        return (y - 1) * 365 + n if y <= 1752 else (y - 2) * 365 + n + 354

    def days_in_month(m, y):
        n = 0
        list_31 = [1, 3, 5, 7, 8, 10, 12]
        list_30 = [4, 6, 9, 11]
        for num in range(1, m):
            if num in list_31:
                n += 31
            elif num in list_30:
                n += 30
            elif leap_year(y):
                n += 29
            else:
                n += 28
        if y == 1752 and m > 9:
            n -= 11
        return n

    def days_in_days(d, m, y):
        if y == 1752 and m == 9 and (d > 2):
            return d - 11
        return d
    current_days = days_in_days(24, 3, 2437) + days_in_month(3, 2437) + days_in_years(2437)
    return current_days - (days_in_days(date, month, year) + days_in_month(month, year) + days_in_years(year))
