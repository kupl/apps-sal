def count_sheep(n):
    # your code
    str = ""
    for i in range(n):
        str = str + "{} sheep...".format(i+1)
    return str

