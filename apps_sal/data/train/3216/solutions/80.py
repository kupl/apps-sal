import math
def movie(card, ticket, perc):
    #System B
    price_A = 0
    visits = 0
    while math.ceil(card) >= price_A:
        price_A += ticket
        card += ticket * (perc ** visits)
        visits += 1
    return visits -1
