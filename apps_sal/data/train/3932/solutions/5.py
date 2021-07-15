def luxhouse(houses):
    return [max(0, max(houses[h+1:])-houses[h]+1) for h in range(len(houses)-1)]+[0]
