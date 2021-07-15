def gimme(i):
    if i[0]> i[1] and i[0]<i[2]:
        return 0
    elif i[0]> i[2] and i[0]<i[1]:
        return 0 
    elif i[1]> i[0] and i[1]<i[2]:
        return 1
    elif i[1]> i[2] and i[1]<i[1]:
        return 1
    elif i[2]> i[1] and i[2]<i[0]:
        return 2 
    elif i[2]> i[0] and i[2]<i[1]:
        return 2
    else : 
        return 1
    

