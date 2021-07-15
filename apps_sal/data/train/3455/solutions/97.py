def disarium_number(number):
    digits = [int(n) for n in str(number)]
    new_number = sum(n ** (i + 1) for i, n in enumerate(digits))
    return "Disarium !!" if new_number == number else "Not !!"
