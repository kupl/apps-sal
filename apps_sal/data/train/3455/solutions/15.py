def disarium_number(number):
    disarium_sum = sum((int(digit) ** pos for (pos, digit) in enumerate(str(number), 1)))
    if disarium_sum == number:
        return 'Disarium !!'
    return 'Not !!'
