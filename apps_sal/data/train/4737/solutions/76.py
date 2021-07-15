def fuel_price(l, ppl):
    if(l >= 10):
        ppl -= .25 
        return round(l * ppl, 2)
    elif(l >= 8):
        ppl -= .20
        return round(l * ppl, 2)
    elif(l >= 6):
        ppl -= .15
        return round(l * ppl, 2)
    elif(l >= 4):
        ppl -= .10
        return round(l * ppl, 2)
    elif(l >= 2):
        ppl -= .05
        return round(l * ppl, 2)
    return round(l * ppl, 2)
