region1 = "qwertyuiop"
region2 = "asdfghjkl"
region3 = "zxcvbnm,."


def encrypt(text, encryptKey):
    print(text)
    print(encryptKey)
    s = str(encryptKey)
    if len(s) == 1:
        s = ['0', '0', encryptKey]
    elif len(s) == 2:
        s = ['0', s[0], s[1]]
    else:
        s = str(encryptKey)

    ntext = ''
    for c in text:
        if c.lower() in region1:
            ind = region1.find(c.lower())
            if c == c.lower():
                ntext += region1[(ind + int(s[0])) % 10]
            else:
                ntext += region1[(ind + int(s[0])) % 10].upper()
        elif c.lower() in region2:
            ind = region2.find(c.lower())
            if c == c.lower():
                ntext += region2[(ind + int(s[1])) % 9]
            else:
                ntext += region2[(ind + int(s[1])) % 9].upper()
        elif c.lower() in region3 + '<>':
            if c.lower() in region3:
                ind = region3.find(c.lower())
                if c == c.lower():
                    ntext += region3[(ind + int(s[2])) % 9]
                else:
                    if region3[(ind + int(s[2])) % 9] == ',':
                        ntext += '<'
                    elif region3[(ind + int(s[2])) % 9] == '.':
                        ntext += '>'
                    else:
                        ntext += region3[(ind + int(s[2])) % 9].upper()
            if c == '<':
                ind = region3.find(',')
                q = region3[(ind + int(s[2])) % 9]
                if q == ',':
                    ntext += '<'
                elif q == '.':
                    ntext += '>'
                else:
                    ntext += q.upper()
            if c == '>':
                ind = region3.find('.')
                q = region3[(ind + int(s[2])) % 9]
                if q == ',':
                    ntext += '<'
                elif q == '.':
                    ntext += '>'
                else:
                    ntext += q.upper()

        else:
            ntext += c
    print(ntext)
    return ntext


def decrypt(text, encryptKey):
    print(text)
    print(encryptKey)

    s = str(encryptKey)
    if len(s) == 1:
        s = ['0', '0', encryptKey]
    elif len(s) == 2:
        s = ['0', s[0], s[1]]
    else:
        s = str(encryptKey)

    ntext = ''
    for c in text:
        if c.lower() in region1:
            ind = region1.find(c.lower())
            if c == c.lower():
                ntext += region1[(ind - int(s[0])) % 10]
            else:
                ntext += region1[(ind - int(s[0])) % 10].upper()
        elif c.lower() in region2:
            ind = region2.find(c.lower())
            if c == c.lower():
                ntext += region2[(ind - int(s[1])) % 9]
            else:
                ntext += region2[(ind - int(s[1])) % 9].upper()
        elif c.lower() in region3 + '<>':
            if c.lower() in region3:
                ind = region3.find(c.lower())
                if c == c.lower():
                    ntext += region3[(ind - int(s[2])) % 9]
                else:
                    if region3[(ind - int(s[2])) % 9] == ',':
                        ntext += '<'
                    elif region3[(ind - int(s[2])) % 9] == '.':
                        ntext += '>'
                    else:
                        ntext += region3[(ind - int(s[2])) % 9].upper()
            if c == '<':
                ind = region3.find(',')
                q = region3[(ind - int(s[2])) % 9]
                if q == ',':
                    ntext += '<'
                elif q == '.':
                    ntext += '>'
                else:
                    ntext += q.upper()
            if c == '>':
                ind = region3.find('.')
                q = region3[(ind - int(s[2])) % 9]
                if q == ',':
                    ntext += '<'
                elif q == '.':
                    ntext += '>'
                else:
                    ntext += q.upper()

        else:
            ntext += c
    print(ntext)
    return ntext
