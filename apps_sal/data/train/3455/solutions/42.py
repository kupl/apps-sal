def disarium_number(number):
    big_number = 0
    i = 1
    for dig in str(number):
        big_number += pow(int(dig), i)
        i += 1
    if big_number == number:
        return "Disarium !!"
    else:
        return "Not !!"
