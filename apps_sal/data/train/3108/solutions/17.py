def multi_table(number):
    return "".join([str(x) + " * " + str(number) + " = " + str(x * number) + "\n" for x in range(1, 11)])[:-1]
