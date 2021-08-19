def first_non_repeated(string):
    for i in range(len(string.upper())):
        e = string[i]
        if string.lower().count(e) == 1:
            return e
    return None
