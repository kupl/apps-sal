def jumping_number(number):
    curr = int(str(number)[0])
    number = str(number)[1:]
    for el in number:
        if int(el) - int(curr) != 1 and int(curr) - int(el) != 1:
            return "Not!!"
        curr = el
    return "Jumping!!"
