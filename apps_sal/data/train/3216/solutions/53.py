import math
def movie(card, ticket, perc):
    i = 1
    lhs = lambda: ticket * i
    rhs = lambda: math.ceil(card + ticket*(1-perc**i)/(1-perc))
    
    while lhs() <= rhs():
        i += 1
        
    return i-1
