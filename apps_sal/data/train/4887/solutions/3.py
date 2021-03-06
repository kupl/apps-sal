def days(date, month, year):

    def day_calc(date, month, year):
        count = 0
        for i in range(0, year):
            if i < 1752:
                if i % 4 == 0:
                    count += 366
                else:
                    count += 365
            elif i == 1752:
                count += 366 - 11
            elif i % 400 == 0:
                count += 366
            elif i % 100 == 0:
                count += 365
            elif i % 4 == 0:
                count += 366
            else:
                count += 365
        months = {0: 0, 1: 31, 2: 59, 3: 90, 4: 120, 5: 151, 6: 181, 7: 212, 8: 243, 9: 273, 10: 304, 11: 334, 12: 365}
        if year % 400 == 0:
            count += months[month - 1]
            if month > 2:
                count += 1
        elif year % 100 == 0:
            count += months[month - 1]
        elif year % 4 == 0:
            count += months[month - 1]
            if month > 2:
                count += 1
        else:
            count += months[month - 1]
        if year == 1752 and month == 9 and (date > 13):
            count += date - 11
        else:
            count += date
        return count
    cdate = 24
    cmonth = 3
    cyear = 2437
    return day_calc(cdate, cmonth, cyear) - day_calc(date, month, year)


print(days(31, 1, 2436))
