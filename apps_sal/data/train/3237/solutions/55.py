def even_or_odd(number):
    try:
        if number % 2 == 0:
            return 'Even'
        elif number % 2 == 1:
            return 'Odd'
    except:
        print('error: not a number')
