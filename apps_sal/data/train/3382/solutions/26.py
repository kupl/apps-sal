def lowercase_count(string):
    c = 0
    for i in string:
        if i.islower() == True:
            c += 1
    return c
