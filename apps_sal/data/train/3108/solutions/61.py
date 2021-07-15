def multi_table(number):
    out = ""
    for i in range(1, 11):
        out+=str(i) + " * " + str(number) + " = " + str(i*number) +"\n"
    return out.strip("\n")
