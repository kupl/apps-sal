def disarium_number(number):
    return 'Disarium !!' if number == sum((int(d) ** (i + 1) for (i, d) in enumerate(str(number)))) else 'Not !!'
