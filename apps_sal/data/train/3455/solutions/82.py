def disarium_number(number):
    n = []
    a = 0
    for i in str(number):
        n.append(int(i))
    for i in range(len(n)):
        a += int(n[i])**int(i + 1)
    return "Disarium !!" if a == number else "Not !!"
