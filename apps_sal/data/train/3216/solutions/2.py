from itertools import count
from math import ceil


def movie(card, ticket, perc):
    return next((n for n in count(1) if ceil(card + ticket * perc * (1 - perc ** n) / (1 - perc)) < ticket * n))
