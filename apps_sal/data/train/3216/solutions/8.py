def movie(card, ticket, perc, cnt=0):
    while card > -1:
        card += ticket * perc ** cnt * perc - ticket
        cnt += 1
    return cnt
