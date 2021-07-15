def disarium_number(number):
    output = 0
    for i in range(0,len(str(number))):
        output += int(str(number)[i])**(i+1)
    if output == number:
        return "Disarium !!"
    return "Not !!"
