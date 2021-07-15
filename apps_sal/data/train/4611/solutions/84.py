def animals(heads, legs):
    if heads == 0 and legs == 0:            # (0, 0) return (0, 0)
        return (0, 0)
    elif heads <= 0 or legs <= 0:
        return "No solutions"
    elif heads > 0 and legs > 0:
        x = -legs/2 + 2*heads
        y = legs/2 - heads
        if legs % 2 == 0 and x >= 0 and y >= 0: 
            return (x, y)
        else:
            return "No solutions"
    else:
        return "No soultions"
         
        
        
        
        
        
        

