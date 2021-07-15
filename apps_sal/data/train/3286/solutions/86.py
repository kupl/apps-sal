def enough(maximal, drin, warten):
    pers = drin + warten
    
    if pers <= maximal:
        return 0 
    elif pers > maximal:
        return pers - maximal
