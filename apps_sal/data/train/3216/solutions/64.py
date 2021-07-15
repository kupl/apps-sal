import math

def movie(card, ticket, perc):
    temp, spend_a, spend_b = 1, 0, 0
    
    while spend_a <= math.ceil(spend_b):
        
        spend_a += ticket
        
        if temp == 1:
            spend_b += card + ticket * perc
        else:
            spend_b += ticket * math.pow(perc,temp)
        
        temp += 1
        
    return temp-1
