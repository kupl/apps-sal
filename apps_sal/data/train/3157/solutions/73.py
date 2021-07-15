def number(bus_stops):
    enter, leave = zip(*bus_stops)
    return sum(enter) - sum(leave)
