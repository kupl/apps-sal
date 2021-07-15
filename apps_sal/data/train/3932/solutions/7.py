def luxhouse(houses):
    return [(max(houses[i], max(houses[i+1:])+1)) - houses[i] for i in range(len(houses) - 1)] + [0]

