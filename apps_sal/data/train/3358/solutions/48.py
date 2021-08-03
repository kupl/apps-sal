def correct(string):
    newstring = ""
    for item in string:
        if item in ['5', '0', '1']:
            if item == "5":
                newstring = newstring + "S"
            if item == "0":
                newstring = newstring + "O"
            if item == "1":
                newstring = newstring + "I"
        else:
            newstring = newstring + item

    return newstring
