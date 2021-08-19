from itertools import count
from math import ceil


def movie(card, ticket, perc):
    return next((x for x in count(card // ticket) if ticket * x > ceil(card + ticket * perc * (1 - perc ** x) / (1 - perc))))
