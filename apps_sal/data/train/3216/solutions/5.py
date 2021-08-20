from math import ceil


def movie(card, ticket, rate):
    count = 0
    totalA = 0.0
    totalB = 0.0
    while ceil(card + totalB) >= totalA:
        totalA += ticket
        totalB = (totalB + ticket) * rate
        count += 1
    return count
