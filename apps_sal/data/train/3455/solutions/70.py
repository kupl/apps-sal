def disarium_number(number):
    s = 0
    for i in range(len(str(number))):
        s += int(str(number)[i]) ** (i + 1)
    if s == number:
        return "Disarium !!"
    else:
        return "Not !!"
