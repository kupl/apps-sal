def disarium_number(number):
    x = str(number)
    n = 0
    for i in range(len(x)):
        n += (int(x[i]) ** (i + 1))
    return "Disarium !!" if n == number else "Not !!"
