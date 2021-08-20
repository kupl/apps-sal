def number(bus_stops):
    get_in = sum([a[0] for a in bus_stops])
    get_out = sum([a[1] for a in bus_stops])
    total = get_in - get_out
    return total
