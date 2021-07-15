def movie(card, ticket, perc):
    B = card
    A = 0
    n = 0
    t = ticket
    while A <= int(B)+ 1:
        A += ticket
        t *= perc
        B += t
        n += 1
    return n 
