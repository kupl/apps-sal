def tidyNumber(n):
    tidy = True
    for i in range(1, len(str(n))):
        if(int(str(n)[i]) < int(str(n)[i - 1])):
            tidy = False
    return tidy
