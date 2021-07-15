def disarium_number(number):
    return 'Disarium !!' if sum(int(j) ** (i + 1) for i, j in enumerate(list(str(number)))) == number else 'Not !!'
