def disarium_number(number):
    a = [i for i in range(1, len(str(number))+1)]
    b = [int(i) for i in list(str(number))]
    c = [x**y for x, y in zip(b, a)]
    return "Disarium !!" if sum(c) == number else "Not !!"
