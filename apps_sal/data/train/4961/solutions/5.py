def box(coords):
    nw,se = [0,0],[0,0]
    for y,x in coords:
        if x<nw[1]:
            nw[1] = x    
        if y>nw[0]:
            nw[0] = y      
        if x>se[1]:
            se[1] = x        
        if y<se[0]:
            se[0] = y
    return {'nw':nw,'se':se}
