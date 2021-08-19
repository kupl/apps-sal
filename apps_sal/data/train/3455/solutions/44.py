def disarium_number(number):
    res = 0
    for i in range(len(str(number))):
        res += int(str(number)[i]) ** (i + 1)
    if number == res:
        return 'Disarium !!'
    return 'Not !!'
