def luxhouse(houses):
    maxh = [houses[i] for i in range(len(houses))]
    maxh[-1] = houses[-1]
    for i in range(len(houses)-2, -1, -1):
        maxh[i] = max(maxh[i], maxh[i+1])
    for i in range(len(houses)-1):
        if maxh[i] == maxh[i+1]:
            maxh[i] += 1
    return [maxh[i]-houses[i] for i in range(len(houses))]
