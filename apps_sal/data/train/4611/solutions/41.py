def animals(heads, legs):    
    if heads==0 and legs==0:
        return (0,0)
    
    cows =((legs) - 2*heads) / 2
    chicks = heads-cows
    
    if cows == int(cows) and chicks>=0 and cows>=0:
        return (chicks, cows)
    else:return "No solutions"
