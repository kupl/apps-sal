def leap(year):
    if year < 1753:
        if year % 4 == 0:
            return True
    elif year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
    else:
        return False


def days(date, month, year):
    the_date = [24, 3, 2437]
    Leap_year = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    Non_leap_year = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    point_date = [date, month, year]
    reverse_date = [year, month, date]
    days_from_beginning = the_date[0]
    for i in range(1, the_date[1]):
        days_from_beginning += Non_leap_year[i]

    def to_year_end(list, dict):
        days_to_end = dict[list[1]] - list[0]
        for i in range(list[1] + 1, 13):
            days_to_end += dict[i]
        return days_to_end
    if year == the_date[2] and month == the_date[1]:
        result = the_date[0] - date
        return result
    elif year == the_date[2] and month < the_date[1]:
        result = days_from_beginning - date
        for i in range(1, month):
            result -= Non_leap_year[i]
        return result
    else:
        result = days_from_beginning
        if reverse_date < [1752, 9, 14]:
            result -= 11
        if leap(year):
            result += to_year_end(point_date, Leap_year)
        else:
            result += to_year_end(point_date, Non_leap_year)
        for y in range(year + 1, the_date[2]):
            if leap(y):
                result += 366
            else:
                result += 365
        return result
