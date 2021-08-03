def disarium_number(number):
    if number == sum(int(n)**(i + 1) for i, n in enumerate(str(number))):
        return "Disarium !!"
    else:
        return "Not !!"
