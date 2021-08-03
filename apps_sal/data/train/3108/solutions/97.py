def multi_table(n):
    x = ""
    for i in range(1, 11):
        x += "{} * {} = {}\n".format(i, n, i * n)
    return x[:-1]
