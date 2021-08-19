def arbitrate(bus_str, n):
    return ''.join(['0' if i != bus_str.find('1') else '1' for (i, x) in enumerate(bus_str)])
