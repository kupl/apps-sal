def luxhouse(houses):
    return [max(0, max(houses[i:]) - h + 1) for i, h in enumerate(houses[:-1], 1)] + [0]
