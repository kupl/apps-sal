def century(year):
    s = str(year)
    if year <= 100:
        return 1
    else:
        if year %100 == 0:
            return int(s[:-2])
        else:
            return 1 + int(s[:-2])
