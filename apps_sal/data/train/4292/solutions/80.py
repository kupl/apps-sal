def string_clean(s):
    """
    Function will return the cleaned string
    """
    wordclean = list(s)
    fini = []
    for i in wordclean:
        if i.isnumeric():
            a = 1
        else:
            fini.append(i)
    return "".join(fini)
