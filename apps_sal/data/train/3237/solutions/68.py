def even_or_odd(number):
    
    if type(number) == int and number % 2 == 0:
        return "Even"
    elif type(number) == int and number % 2 != 0:
        return "Odd"
    else:
        return "Parameter needs to be an integer."
