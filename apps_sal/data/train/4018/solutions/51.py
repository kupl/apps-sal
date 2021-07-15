def isDigit(string):
    string = string.replace(".", "")
    string = string.strip()
    if string and string[0]== "-":
        string = string.replace("-","")
    return string.isdigit()
