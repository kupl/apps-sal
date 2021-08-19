def increment_string(strng):
    lastnonnum = 0
    for x in range(0, len(strng)):
        if not strng[x].isnumeric():
            lastnonnum = x
    for x in range(lastnonnum, len(strng)):
        if strng[x].isnumeric():
            print(strng[x])
            number = strng[x:len(strng)]
            newnumber = str(int(number) + 1)
            while len(number) > len(newnumber):
                newnumber = '0' + newnumber
            strng = strng[0:x] + newnumber
            return strng
    return strng + '1'
