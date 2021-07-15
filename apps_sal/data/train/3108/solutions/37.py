def multi_table(number):
    tab = ""
    for n in range(1, 11):
        r = n * number
        tab += f'{n} * {number} = {r}'
        if n < 10:
            tab += "\n"
    return tab
