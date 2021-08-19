from itertools import takewhile, count, accumulate


def movie(card, ticket, perc):
    sys_b = accumulate((ticket * perc ** n for n in count(1)))
    sys_a = accumulate((ticket for m in count(1)))
    return sum((1 for a in takewhile(lambda x: round(x[0] + card + 0.49) >= x[1], zip(sys_b, sys_a)))) + 1
