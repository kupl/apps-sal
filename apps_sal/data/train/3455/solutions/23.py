def disarium_number(number):
    rs = sum([n ** (i + 1) for (i, n) in enumerate(map(int, str(number)))])
    return 'Disarium !!' if rs == number else 'Not !!'
