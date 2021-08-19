def even_or_odd(number):
    modulo = number % 2
    if modulo == 1:
        return 'Odd'
    elif modulo == 0:
        return 'Even'
