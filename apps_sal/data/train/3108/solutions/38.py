def multi_table(number):
    out = []
    for i in range(1, 11):
        out.append("{} * {} = {}".format(i, number, i * number))
    return "\n".join(out)
