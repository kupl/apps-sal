def london_city_hacker(journey):
    bus_counter = 0
    bus_price = 0
    tube_price = 0
    for i in journey:
        if type(i) is int:
            bus_counter += 1
            if bus_counter > 1:
                bus_counter = 0
                bus_price += 0
            else:
                bus_price += 1.5
        if type(i) is str:
            bus_counter = 0
            tube_price += 2.4
    return f'£{tube_price + bus_price:.2f}'
