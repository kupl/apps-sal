def century(year):
    if year < 100:
        return 1
    elif year < 1000:
        if year % 100 == 0:
            return year // 100
        else:
            return year // 100 + 1
    elif year % 10 == 0 and year // 10 % 10 == 0:
        return int(str(year)[:len(str(year)) - 2])
    else:
        return int(str(year)[:len(str(year)) - 2]) + 1
