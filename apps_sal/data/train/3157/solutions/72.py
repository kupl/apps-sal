def number(bus_stops):
    # Good Luck!
    return sum((peoplein - peopleout) for peoplein,peopleout in (bus_stops))
