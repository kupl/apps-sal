def even_or_odd(number):
    number = int(number)
    if number.__mod__(2) == 0:
        return "Even"
    else:
        return "Odd"
