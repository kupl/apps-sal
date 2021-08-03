def tidyNumber(n):
    tidy = True
    y = ''
    for x in str(n):
        if y != None:
            if x < y:
                tidy = False
            else:
                y = x

    return tidy
