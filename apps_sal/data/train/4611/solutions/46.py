def animals(heads, legs):
    chickens = a =(4*heads - legs)/2
    cows     = b =(legs - 2*heads)/2
    
    if heads == legs == 0                :    return (0,0)
    if a<0 or b<0 or  [a%1,b%1] != [0,0] :    return 'No solutions'
    else                                 :    return (chickens, cows)


