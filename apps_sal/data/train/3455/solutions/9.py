def disarium_number(number):
    return 'Disarium !!' if sum((int(c) ** i for (i, c) in enumerate(str(number), 1))) == number else 'Not !!'
