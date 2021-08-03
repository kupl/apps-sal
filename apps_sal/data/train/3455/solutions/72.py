def disarium_number(number):
    return("Disarium !!" if sum(int(elem)**(i + 1) for i, elem in enumerate(str(number))) == number else "Not !!")
