def century(year):
    if year > 99:
        if int(str(year)[2:]) > 0:
            return int(str(year)[:-2]) + 1
        else:
            return int(str(year)[:-2])
    elif year > 0:
        return 1
    else:
        return 0
