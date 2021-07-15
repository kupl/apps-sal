def over_the_road(ad, n):
    od = list(range(1, n*2, 2))
    ev = list(range(n*2, 0,-2))
    return od[ev.index(ad)] if ad %2 == 0 else ev[od.index(ad)]
# Flez

