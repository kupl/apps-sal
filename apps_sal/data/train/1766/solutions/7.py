def skrzat(base, number):
    s = 2863311530
    if base == 'b':
        i = int(number, 2)
        return f'From binary: {number} is {(s ^ i) - s}'
    elif base == 'd':
        return f'From decimal: {number} is {number + s ^ s:b}'
