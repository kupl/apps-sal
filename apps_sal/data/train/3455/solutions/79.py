def disarium_number(number):
    print(number)
    return 'Disarium !!' if sum((int(d) ** (i + 1) for (i, d) in enumerate(f'{number}'))) == number else 'Not !!'
