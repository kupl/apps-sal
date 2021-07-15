def movie(card, ticket, perc):
    print((card, ticket, perc))
    import math
    total_ticket = 0.0
    total_card = card
    count = 0
    movieprice_bycard = ticket
    while total_ticket <= math.ceil(total_card):
        count += 1
        movieprice_bycard *= perc
        total_ticket += ticket
        total_card += movieprice_bycard
    return count

