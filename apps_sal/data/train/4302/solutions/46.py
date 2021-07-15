def better_than_average(cp, yp):
    a = 0
    for x in cp:
        a +=x
    return (a+yp)/(len(cp)+1) < yp

    

