def century(year):
    div = year // 100
    rest = year % 100
    if rest == 0:
        return div
    else:
        return div + 1
