def disarium_number(number):
    digits = str(number)
    return 'Disarium !!' if sum((int(digits[i]) ** (i + 1) for i in range(len(digits)))) == number else 'Not !!'
