def multi_table(number):
    table = ""
    for i in range(1, 11):
        table += "{} * {} = {}\n".format(i, number, i * number)
    table = table.rstrip("\n")
    return table
