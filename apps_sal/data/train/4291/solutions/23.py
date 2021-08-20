def century(year):
    year = str(year)
    if len(year) < 3:
        return 1
    elif len(year) == 3 and len(year) < 4:
        x = int(year[1] + year[2])
        if x >= 1 and x <= 99:
            return int(year[0]) + 1
        else:
            return int(year[0])
    elif len(year) == 4 and len(year) < 5:
        x = int(year[2] + year[3])
        if x >= 1 and x <= 99:
            return int(year[0] + year[1]) + 1
        else:
            return int(year[0] + year[1])
    elif len(year) == 5 and len(year) < 6:
        x = int(year[3] + year[4])
        if x >= 1 and x <= 99:
            return int(year[0] + year[1] + year[2]) + 1
        else:
            return int(year[0] + year[1] + year[2])
    elif len(year) == 6 and len(year) < 7:
        x = int(year[4] + year[5])
        if x >= 1 and x <= 99:
            return int(year[0] + year[1] + year[2] + year[3]) + 1
        else:
            return int(year[0] + year[1] + year[2] + year[3])
    elif len(year) == 7 and len(year) < 8:
        x = int(year[5] + year[6])
        if x >= 1 and x <= 99:
            return int(year[0] + year[1] + year[2] + year[3] + year[4]) + 1
        else:
            return int(year[0] + year[1] + year[2] + year[3] + year[4])
    elif len(year) == 8 and len(year) < 9:
        x = int(year[6] + year[7])
        if x >= 1 and x <= 99:
            return int(year[0] + year[1] + year[2] + year[3] + year[4] + year[5]) + 1
        else:
            return int(year[0] + year[1] + year[2] + year[3] + year[4] + year[5])
