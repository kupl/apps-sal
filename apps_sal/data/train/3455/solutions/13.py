def disarium_number(number):
    return "Disarium !!" if sum(int(v) ** (i + 1) for i, v in enumerate(str(number))) == number else "Not !!"
