from math import ceil


def movie(card, ticket, perc):
    answer = 1
    systemA = 0
    systemB = card
    while answer > 0:
        systemA += ticket
        systemB += ticket * perc ** answer
        if ceil(systemA) > ceil(systemB):
            return answer
        answer += 1
