def disarium_number(number):
    n = str(number)
    x = 0
    for i in range(0, len(str(number))):
        x = x + int(n[i])**(i + 1)
    if x == number:
        return "Disarium !!"
    return "Not !!"
