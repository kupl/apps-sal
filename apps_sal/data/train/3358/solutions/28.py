def correct(string):
    for strings in string:
        if strings.isdigit():
            string = string.replace("5","S")
            string = string.replace("0","O")
            string = string.replace("1","I")
    return string

