def to_alternating_case(string):
    strX = ""
    for i in range(len(string)):
        if string[i].isupper():
            strX += string[i].lower()
        elif string[i].islower():
            strX += string[i].upper()
        else:
            strX += string[i]
    return strX
