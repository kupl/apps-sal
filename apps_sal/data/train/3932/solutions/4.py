def luxhouse(houses):
    return [max(max(houses[i+1:])-j+1,0) for i,j in enumerate(houses[:-1])] +[0]
