def crap(garden, bags, cap):
    for each in garden:
        for i in each:
            if i == 'D':
                return 'Dog!!'
    a = 0
    for each in garden:
        for i in each:
            if i == '@':
                a +=1
    b = bags * cap
    if a > b:
        return 'Cr@p'
    else:
        return "Clean"

