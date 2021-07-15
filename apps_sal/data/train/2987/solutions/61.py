def is_divide_by(number, a, b):
    '''
    Dado un numero int <number> y otros dos nuemeros int <a> y <b>, 
    devuelve el valor de verdad True si <number> es divisible por <a> y <b>
    y False de otro modo
    '''
    return number % a == 0 and number % b == 0
