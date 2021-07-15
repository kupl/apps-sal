def multi_table(number):
    a = ["{} * {} = {}".format(i,number,i*number) for i in range(1,11)]
    return "\n".join(a)
