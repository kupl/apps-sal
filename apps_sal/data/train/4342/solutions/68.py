def no_space(x):
    lst = x.strip().split()
    strin = ''
    for el in lst:
        if el:
            strin += el

    return strin
