def tram(stops, off, on):
    total = 0
    passengers = []
    for i in range(stops):
        total += on[i] - off[i]
        passengers.append(total)
    return max(passengers)
