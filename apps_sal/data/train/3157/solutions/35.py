def number(bus_stops):
    numOfPassengers = 0
    index = 0
    for x in range(0,len(bus_stops)):
        numOfPassengers += bus_stops[index][0]
        numOfPassengers -= bus_stops[index][1]
        index += 1
    return numOfPassengers
    

