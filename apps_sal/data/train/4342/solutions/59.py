def no_space(x):
    x1 = ''
    for i in range(len(x)):
        if x[i].isspace() == True:
            pass
        else:
            x1 += x[i]
    return x1
