def disarium_number(number):
    return 'Disarium !!' if sum((int(v) ** (k + 1) for (k, v) in enumerate(str(number)))) == number else 'Not !!'
