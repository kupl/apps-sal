def disarium_number(number):
    return 'Disarium !!' if sum((int(n) ** i for (i, n) in enumerate(str(number), 1))) == number else 'Not !!'
