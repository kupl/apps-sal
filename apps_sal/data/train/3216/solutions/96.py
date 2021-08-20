from math import ceil


def movie(card, ticket, rate):
    count = 0
    totala = 0.0
    totalb = 0.0
    while ceil(card + totalb) >= totala:
        totala += ticket
        totalb = (totalb + ticket) * rate
        count += 1
    return count
