def crap(g, b, c):    
    g = sum(g,[])
    if 'D' in g:   return "Dog!!"    
    return "Clean" if g.count('@') <= b*c else "Cr@p"
