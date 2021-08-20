from itertools import count
from math import ceil


def movie(card, ticket, perc):

    def A(n):
        return ticket * n

    def B(n):
        return card + ticket * (perc * (perc ** n - 1) / (perc - 1))
    return next((n for n in count(1) if ceil(B(n)) < A(n)))
