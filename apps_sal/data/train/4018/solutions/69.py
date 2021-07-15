def isDigit(string):
    print(string)
    s = string.lstrip('-')
    print(s.isdigit())
    print(s.isdecimal())
    print(s.isnumeric())
    try:
        float(s)
        print("succes")
        return True
    except:
        return False
