def movie(card, ticket, perc):
    ticketsBought = 0

    a = 0
    b = card
    while (round(b,0) >= a):
        discount = pow(perc, ticketsBought)
        b += ticket * discount
        ticketsBought += 1

        a += ticket
        
    if (b > round(b, 0)):
        b += 1
        
    if (a > b):
        return ticketsBought - 1
    else:
        ticketsBought += 1
        return ticketsBought -1
        
    print(f"a:{a}, b:{b}")
    print(f"ticketsBought:{ticketsBought - 1}")
    return ticketsBought - 1
