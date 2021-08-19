def disarium_number(number):
    return 'Disarium !!' if sum([int(x) ** (y + 1) for (y, x) in enumerate(str(number))]) == number else 'Not !!'
