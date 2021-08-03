def multi_table(number):
    rez = ""
    for i in range(1, 11):
        rez += str(i) + " * " + str(number) + " = " + str(i * number)
        if i < 10:
            rez += "\n"
    return rez
