import math
def movie(card, ticket, perc):
    sysA = ticket
    sysB = ticket*perc
    count = 1
    while card+math.ceil(sysB) >= sysA:
        sysA+=ticket
        sysB = (sysB) + (ticket)*(perc**(count+1))
        count+=1
        
    return count
