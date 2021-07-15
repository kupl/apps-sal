def alternateCase(s):
    string = ''
    for i in s:
        print(i)
        if i == i.upper():
            string += i.lower()
        else:
            string += i.upper()
    return string
