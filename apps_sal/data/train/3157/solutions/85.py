def number(bus_stops):
    people = [sum(i) for i in zip(*bus_stops)]
    return people[0] - people[1]
