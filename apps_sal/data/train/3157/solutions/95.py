def number(bus_stops):
    people=0
    for tuple in bus_stops:
        x,y = tuple
        people+=x-y
        
    return people

