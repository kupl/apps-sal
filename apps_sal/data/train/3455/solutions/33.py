def disarium_number(number):
    return "Disarium !!" if sum(int(ch) ** i for i, ch in enumerate(str(number), start=1)) == number else "Not !!"
