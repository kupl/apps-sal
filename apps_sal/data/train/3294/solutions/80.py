def converter(mpg):
    '''
    takes miles per gallon as input
    converts it to kilometers per hour
    '''
    ans = (mpg*1.609344)/4.54609188
    return round(ans,2)
