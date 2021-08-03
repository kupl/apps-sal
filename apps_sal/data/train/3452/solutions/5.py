def snail(column, day, night):

    heightUpColumn = 0
    daysPassed = 1

    while heightUpColumn < column:
        heightUpColumn += day
        if heightUpColumn < column:
            heightUpColumn -= night
            daysPassed += 1
        elif heightUpColumn >= column:
            return daysPassed
