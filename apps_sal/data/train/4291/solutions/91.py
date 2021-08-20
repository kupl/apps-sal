def century(year):
    return year // 100 if year / 100 % 1 == 0 else year // 100 + 1
