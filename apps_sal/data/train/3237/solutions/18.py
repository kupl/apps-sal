def even_or_odd(number):
    if not isinstance(number, int):
        raise Exception('The input is not an integer')
    if number % 2 == 0:
        return 'Even'
    return 'Odd'
