def even_or_odd(number):
    if(number < 0):
        number = -1 * number
    if(number % 2 == 0 or number == 0):
        return "Even"
    else:
        return "Odd"
