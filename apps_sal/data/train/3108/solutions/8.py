def multi_table(number):
    return "\n".join(["{0} * {1} = {2}".format(str(i), str(number), str(i * number)) for i in range(1, 11)])
