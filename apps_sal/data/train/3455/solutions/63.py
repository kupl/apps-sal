def disarium_number(number):
    digits = list(str(number))
    a = 0
    for (index, digit) in enumerate(digits):
        a += int(digit) ** (index + 1)
    return 'Disarium !!' if a == number else 'Not !!'
