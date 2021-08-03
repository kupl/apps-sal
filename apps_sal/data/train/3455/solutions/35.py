def disarium_number(number):

    x = []
    z = 0
    y = 1

    for i in str(number):
        x.append(int(i))

    for i in x:
        z += i**y
        y += 1

    if number == z:
        return "Disarium !!"
    else:
        return "Not !!"
