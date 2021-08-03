def bus_timer(time):
    c = time.split(":")
    z = int(c[1]) + 5
    t = 0
    if int(c[0]) == 23 and int(c[1]) >= 55:
        c[0] = 0
        c[1] = (int(c[1]) + 5) - 60
        if int(c[1]) == 0:
            t = 0
        elif int(c[1]) > 0:
            t = (((5 - int(c[0])) * 60) + (60 - int(c[1])))
    elif int(c[0]) == 5 and int(c[1]) >= 55:
        c[0] = 6
        c[1] = (int(c[1]) + 5) - 60
        if int(c[1]) == 0:
            t = 0
        elif int(c[1]) > 0:
            t = 15 - int(c[1])
    elif int(c[0]) < 6:
        if int(c[1]) == 0:
            t = ((6 - int(c[0])) * 60) - 5
        elif int(c[1]) > 0:
            t = (((5 - int(c[0])) * 60) + (60 - int(c[1]))) - 5
    else:
        if z > 60:
            z = z - 60
        if z < 15:
            t = 15 - z
        elif z > 15 and z < 30:
            t = 30 - z
        elif z > 30 and z < 45:
            t = 45 - z
        elif z > 45:
            t = 60 - z
    return t
