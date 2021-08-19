def sum_digits(number):
    s = 0
    n = str(number)
    for i in n:
        if i.isdigit():
            s += int(i)
    return s
