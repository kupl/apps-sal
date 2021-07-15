def even_or_odd(number):
    if not isinstance(number, int):
        print('This is not an integer')
    elif number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
