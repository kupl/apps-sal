def even_or_odd(number):
    string = ""

    if (number & (1 >> 0)):
        string = "Odd"
    else:
        string = "Even"
    return string
