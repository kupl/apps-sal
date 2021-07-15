def meeting(rooms):
    for x in rooms:
        if (x is 'O'):
            return(rooms.index(x))
    return('None available!')

