def sum_digits(number):
    kol = 0
    j = ""
    string = str(number)
    for i in string:
        j = ""
        if i == "-":
            continue
        else:
            j += i
        kol += int(j)
    return kol
