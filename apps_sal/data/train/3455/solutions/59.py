def disarium_number(number):
    s = sum(n ** (i + 1) for i, n in enumerate(map(int, str(number))))
    return 'Disarium !!' if s == number else 'Not !!'
