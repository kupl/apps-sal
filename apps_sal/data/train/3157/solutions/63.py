def number(bus_stops):
    lastPeople = 0
    i = 0
    while(i< len(bus_stops)): 
        lastPeople = lastPeople + bus_stops[i][0] - bus_stops[i][1]
        i = i+1
    return lastPeople;
