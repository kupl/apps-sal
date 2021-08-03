def even_or_odd(number):

    if type(number) == int:
        return "Even" if number % 2 == 0 else "Odd"
    else:
        return "Parameter needs to be an integer."
