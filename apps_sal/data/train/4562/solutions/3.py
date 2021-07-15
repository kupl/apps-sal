def snap(flash_pile, turtle_pile, snapper=0):
    new_pile=['']
    if len(turtle_pile)<=0: return snapper
        
    for x in range(len(turtle_pile)):
        
        new_pile.append(flash_pile[x])
        if isSnap(new_pile): return snap(flash_pile[x+1:]+new_pile[1:],turtle_pile[x:],snapper+1)
            
        new_pile.append(turtle_pile[x])
        if isSnap(new_pile): return snap(flash_pile[x+1:]+new_pile[1:],turtle_pile[x+1:],snapper+1)
        
    return snapper
    
      
def isSnap(pile):
    return pile[-1]==pile[-2]
