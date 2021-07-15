def disarium_number(number):
    return "Disarium !!" if sum(int(digit) ** i for i,digit in enumerate(str(number), start=1)) == number else "Not !!"
