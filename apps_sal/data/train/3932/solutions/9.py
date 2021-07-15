def luxhouse(houses):
    return [0 if not houses[i + 1:] else max(max(houses[i + 1:]) + 1 - houses[i], 0) for i in range(len(houses))]
