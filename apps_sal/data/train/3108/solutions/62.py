def multi_table(number):
    table = "1 * " + str(number) + " = " + str(number * 1)
    for x in range(9):
        x += 2
        table = table + "\n" + str(x) + " * " + str(number) + " = " + str(number * x)
    return table
