def century(year):
    return 1 + year // 100 if year % 100 != 0 else year / 100
