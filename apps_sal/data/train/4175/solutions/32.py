def repeater(string, n):
    newstring = ""
    count = n
    while count > 0:
        newstring += string
        count += -1
    return newstring
