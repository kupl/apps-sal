def min_value(digits):
    digits = int(str(((((''.join(str((sorted(set(digits))))).strip(',')).strip('[')).strip(']')).replace(',',''))).replace(" ",''))
    return digits
