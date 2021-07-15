def disarium_number(number):
    result = sum(int(d) ** i for i, d in enumerate(str(number), 1))
    return "Disarium !!" if result == number else "Not !!"
