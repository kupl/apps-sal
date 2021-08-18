def alternateCase(s):
    newstring = ''
    count1 = 0
    count2 = 0
    count3 = 0
    for a in s:
        if (a.isupper()) == True:
            count1 += 1
            newstring += (a.lower())
        elif (a.islower()) == True:
            count2 += 1
            newstring += (a.upper())
        elif (a.isspace()) == True:
            count3 += 1
            newstring += a
    return newstring
