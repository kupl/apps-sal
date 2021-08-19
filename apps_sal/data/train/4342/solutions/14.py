def no_space(x):
    string = ''
    for i in x:
        if i.isspace() == False:
            string += i
    return string
