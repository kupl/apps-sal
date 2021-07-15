def bumps(road):
    countN=0
    countUnderscore=0
    listletters=[char for char in road]
    for i in listletters:
        if i=='n':
            countN+=1
        else:
            countUnderscore+=1
    if countN>15:
        return "Car Dead"
    else:
        return "Woohoo!"
