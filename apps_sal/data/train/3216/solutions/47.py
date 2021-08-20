from math import ceil


def movie(card, ticket, perc):
    (priceOfSystemA, priceOfSystemB, n, ticketPriceB) = (0, card, 0, ticket)
    while ceil(priceOfSystemB) >= priceOfSystemA:
        n += 1
        priceOfSystemA += ticket
        ticketPriceB *= perc
        priceOfSystemB += ticketPriceB
    return n
