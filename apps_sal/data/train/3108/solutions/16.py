def multi_table(number):
    table = ""
    for each in range(1, 11):
        table += "%d * %d = %d\n" % (each, number, each * number)
        
    return table[:-1]
