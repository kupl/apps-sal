def century(year):
    result=0
    if year%100== 0:
        cent= year//100
    else:
        cent=year//100 + 1
    return cent
