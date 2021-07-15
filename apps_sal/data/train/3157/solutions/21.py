def number(bus_stops):
    # Good Luck!
    totalPeople = 0
    for i in bus_stops:
        totalPeople += i[1] - i[0]
    return abs(totalPeople)
    

