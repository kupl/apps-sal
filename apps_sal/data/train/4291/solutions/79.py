def century(year):
    century = year // 100
    decade = year % 100

    if decade > 0:
        return century + 1

    else:
        return century
