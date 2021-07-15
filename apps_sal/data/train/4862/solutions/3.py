def put_the_cat_on_the_table(cat, room):
    if cat[0] < 0 or cat[0] >= len(room) or cat[1] < 0 or cat[1] >= len(room[0]):
        return "NoCat"
    tableCoord = [-1, -1]
    for row in range(len(room)):
        for col in range(len(room[row])):
            if room[row][col]==1:
                tableCoord[0] = row
                tableCoord[1] = col
    if tableCoord == [-1, -1]:
        return "NoTable"
    if cat == tableCoord:
        return ""
    move = [0, 0]
    move[0] = tableCoord[0] - cat[0]
    move[1] = tableCoord[1] - cat[1]
    
    retStr = ""
    while move != [0, 0]:
        if move[0] > 0:
            retStr += "D"
            move[0] -= 1
        if move[0] < 0:
            retStr += "U"
            move[0] += 1
        if move[1] > 0:
            retStr += "R"
            move[1] -= 1
        if move[1] < 0:
            retStr += "L"
            move[1] += 1
    return retStr
