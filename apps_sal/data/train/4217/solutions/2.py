import calendar
DICT = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}


def solve(a, b):
    extended_weekends_list = []
    for year in range(a, b + 1):
        for month in range(1, 13):
            if calendar.monthrange(year, month) == (4, 31):
                extended_weekends_list.append([year, month])
    result = (DICT[extended_weekends_list[0][1]], DICT[extended_weekends_list[-1][1]], len(extended_weekends_list))
    return result
