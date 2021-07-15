def century(year):
    if year <100:
        return 1
    elif year%100 == 0:
        return year//100
    else:
        x = year // 100
        return x+1
