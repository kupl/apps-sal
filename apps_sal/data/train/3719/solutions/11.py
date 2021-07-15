def starting_mark(height):
    if(height < 1.52):
        change_height = 1.52-height
        change_runway = (1.22/float(0.31))*change_height
        return round((9.45-change_runway),2)
    else:
        change_height = height - 1.52
        change_runway = (1.22/float(0.31))*change_height
        return round((9.45 + change_runway),2)
    #your code here

