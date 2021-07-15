def century(year):
    if year%100 == 0:
        return int(year/100)
    else:
        return (int(year/100)+1)
ans=century(89)
