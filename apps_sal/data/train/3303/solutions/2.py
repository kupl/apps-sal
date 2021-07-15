def div_con(x):
    integer = []
    string = []
    for element in x:
        if type(element) == int:
            integer.append(element)
        else:
            string.append(int(element))
    return sum(integer) - sum(string)
