def number(bus_stops):
    get_in = get_out = 0
    for k,v in bus_stops:
        get_in += k
        get_out += v
    return (get_out - get_in) * -1
