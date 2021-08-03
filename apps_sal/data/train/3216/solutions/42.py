def movie(card, ticket, perc):
    temp = ticket
    rA = 0
    rB = card

    while rB > rA - 1:
        temp = temp * perc
        rB += temp
        rA += ticket

    print((str(rB), ":", str(rA)))
    return int(rA / ticket)
