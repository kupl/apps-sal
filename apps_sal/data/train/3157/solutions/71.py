def number(bus_stops):
    peopleInBus=0
    for elem in bus_stops:
        peopleInBus+=elem[0]-elem[1]
    return peopleInBus
