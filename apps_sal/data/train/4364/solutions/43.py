def odd_or_even(arr):
    suma = 0
    result = ''
    if len(arr) == 0:
        result = 'even'
    for x in arr:
        suma = suma +x
        if suma%2 == 0:
            result = 'even'
        else:   
            result = 'odd'
    return result
            

