def disarium_number(number):
    return 'Disarium !!' if sum([int(m) ** (n + 1) for (n, m) in enumerate(str(number))]) == number else 'Not !!'
