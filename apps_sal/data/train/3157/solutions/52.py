def number(bus_stop):
    get_bus = sum([a[0]-a[1] for a in bus_stop])
    if get_bus > 0:
        return get_bus
    else:
        return 0


number([[10,0],[3,5],[5,8]])
number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]])
number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]])

