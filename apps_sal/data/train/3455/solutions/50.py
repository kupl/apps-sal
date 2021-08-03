def disarium_number(number):
    return "Disarium !!" if sum([int(x)**i for i, x in enumerate(list(str(number)), 1)]) == number else "Not !!"
