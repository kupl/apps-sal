def disarium_number(number):
    newNumber = 0
    for index, value in enumerate(str(number)):
        newNumber += int(value)**(int(index) + 1)
    if newNumber == number:
        return "Disarium !!"
    return "Not !!"
