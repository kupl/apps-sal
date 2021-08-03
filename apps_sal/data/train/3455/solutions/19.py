def disarium_number(number):
    b = sum([pow(int(x), i + 1) for i, x in enumerate(str(number))])
    return "Disarium !!" if b == number else "Not !!"
