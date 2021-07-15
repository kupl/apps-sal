def fly_by(lamps, drone):
    newlamps = []
    for x in lamps:
        newlamps.append(x)
        
    for y in range(len(drone)):
        try:
            
            if y <= len(newlamps):
                newlamps[y] = "o"
            else:
                pass
        except:
            pass
         
    return ''.join(newlamps)
    
    
fly_by("xxxxxx","===T")
