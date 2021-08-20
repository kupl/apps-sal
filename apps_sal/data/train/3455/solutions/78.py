def disarium_number(number):
    s = sum((int(x) ** i for (i, x) in enumerate(str(number), 1)))
    return 'Disarium !!' if s == number else 'Not !!'
