def to_alternating_case(string):
    newword=''
    for i in range(len(string)):
        if string[i].isupper() == True:
            newword += string[i].lower()
        elif string[i].islower() == True:
            newword += string[i].upper()
        else:
            newword += string[i]
    return newword
