def converter(mpg):
    res =  (mpg/4.54609188)* 1.609344
    temp = f'{res:.2f}'
    if temp[-1] == '0':
            temp = f'{res:.1f}'
    erg = float(temp)
    return erg

