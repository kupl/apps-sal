def no_space(x):
    finalstring = ''
    for i in x:
        if i in ' ':
            pass
        else:
            finalstring += i
    return finalstring
