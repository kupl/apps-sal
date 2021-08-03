def disarium_number(number):
    disarium = number == sum([int(d)**(i + 1) for i, d in enumerate(str(number))])
    return "Disarium !!" if disarium else "Not !!"
