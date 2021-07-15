def bishop_diagonal(bishop1, bishop2):
    letters = ' abcdefgh'
    x1, y1 = int(letters.index(bishop1[0])), int(bishop1[1])
    x2, y2 = int(letters.index(bishop2[0])), int(bishop2[1])
    if abs(x1 - x2) == abs(y1 - y2):
        xdir = (x1 - x2) // abs(x1 - x2)
        ydir = (y1 - y2) // abs(y1 - y2)
        while 1 < x1 < 8 and 1 < y1 < 8:
            x1 += xdir
            y1 += ydir
        while 1 < x2 < 8 and 1 < y2 < 8:
            x2 -= xdir
            y2 -= ydir
    return sorted([letters[x1] + str(y1), letters[x2] + str(y2)])
