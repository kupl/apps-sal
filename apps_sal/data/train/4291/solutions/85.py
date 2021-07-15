def century(year):
    if year >= 10000:
        return int(year/100)+1 if year%10 == 0 else int(year/100)+1
    else:
        return int(year/100) if year%10 == 0 else int(year/100)+1
