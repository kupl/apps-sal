def movie(card, ticket, perc):
    asum = -1
    cnt = 0
    while card > asum:
        asum += ticket
        card += (ticket * perc**cnt) * perc
        cnt += 1
    return cnt
