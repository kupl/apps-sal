def stringy(size):
    temp = ''
    for el in range(size):
        if el % 2:
            temp += "0"
        else:
            temp += "1"
    return temp

