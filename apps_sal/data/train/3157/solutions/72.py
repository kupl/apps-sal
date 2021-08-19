def number(bus_stops):
    return sum((peoplein - peopleout for (peoplein, peopleout) in bus_stops))
