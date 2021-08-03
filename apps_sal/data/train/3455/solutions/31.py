from math import pow


def disarium_number(number):
    return "Disarium !!" if sum(pow(int(y), x + 1) for x, y in enumerate(str(number))) == number else "Not !!"
