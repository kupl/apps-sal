def spacify(string):
    s = ""
    i = 0
    for char in string:
        if i == 0:
            s = s + string[i]
        else:

            s = s + " " + string[i]
        i += 1

    return s
