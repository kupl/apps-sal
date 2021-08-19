def compare(s1, s2):
    z = 0
    x = 0
    if s1 == None or s1.isalpha() == False:
        s1 = ''
    else:
        for i in range(len(s1)):
            z += ord(s1[i].upper())
    if s2 == None or s2.isalpha() == False:
        s2 = ''
    else:
        for j in range(len(s2)):
            x += ord(s2[j].upper())
    if z == x:
        return True
    else:
        return False
