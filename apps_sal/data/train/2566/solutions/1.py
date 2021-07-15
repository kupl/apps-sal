import calendar

def __starting_point():
    date = list(map(int, input().strip().split(' ')))
    print(calendar.day_name[calendar.weekday(date[2], date[0], date[1])].upper())
__starting_point()
