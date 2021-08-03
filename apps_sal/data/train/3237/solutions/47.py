def even_or_odd(number):

    f = number / 2
    check = f.is_integer()

    if check == True:
        return "Even"
    else:
        return "Odd"
