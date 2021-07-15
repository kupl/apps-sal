def even_or_odd(number):
    modresult = number % 2
    if modresult != 0:
        print("Odd")
        return "Odd"
    else:
        print("Even")
        return "Even"
