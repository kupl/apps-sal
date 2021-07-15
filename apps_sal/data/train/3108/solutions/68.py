def multi_table(number):
    res = ""
    for i in range(1, 11):
        temp = number * i
        res += str(i) + " * " + str(number) + " = " + str(temp) +"\n"
    return res[:-1]
