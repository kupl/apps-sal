def disarium_number(number):
    s = sum((n ** i for (i, n) in enumerate(map(int, str(number)), 1)))
    return 'Disarium !!' if s == number else 'Not !!'
