def movie(card, ticket, perc):
    return next(n for n in range(9**99) if card + ticket*perc*(1-perc**n)/(1-perc) - ticket*n < -1)
