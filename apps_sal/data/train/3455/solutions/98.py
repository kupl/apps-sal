def disarium_number(number):
    return 'Disarium !!' if number == sum((int(digit) ** position for (position, digit) in enumerate(str(number), 1))) else 'Not !!'
