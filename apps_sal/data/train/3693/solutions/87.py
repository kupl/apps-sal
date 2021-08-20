def make_negative(number):
    output = ''
    if number < 0:
        return number
    else:
        output = '-' + str(number)
    return int(output)
