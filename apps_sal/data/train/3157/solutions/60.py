def number(bus_stops):
    people_in_the_bus = 0
    
    for people in bus_stops:
        people_in_the_bus += people[0]
        people_in_the_bus -= people[1]
        
    return people_in_the_bus
