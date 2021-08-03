def alternateCase(s):
    myList = []

    for i in s:
        if i.isupper():
            myList.append(i.lower())
        elif i.islower():
            myList.append(i.upper())
        else:
            myList.append(i)

    return ''.join(myList)
