def disarium_number(number):
    return "Disarium !!" if sum([pow(int(x), i + 1) for i, x in enumerate(list(str(number)))]) == number else "Not !!"
