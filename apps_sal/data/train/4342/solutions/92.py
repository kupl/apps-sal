def no_space(x):
    list = x
    string = ""
    for i in list:
        if i != " ":
            string += i
    return string
