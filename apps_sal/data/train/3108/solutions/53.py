def multi_table(number):
    s = ""
    for x in range(1,11):
        s += f'{x} * {number} = {x * number}\n'
    return s[0:-1]
