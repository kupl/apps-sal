from math import ceil
def movie(card, ticket, perc):
    counter = 0
    sum = card
    perc_= perc
    while ceil(sum) >= ticket*counter:
        sum += ticket*perc_
        perc_ *= perc
        counter += 1
    return counter     
