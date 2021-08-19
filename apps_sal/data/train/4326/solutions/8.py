def london_city_hacker(journey):
    total_cost = 0
    adjacent_bus_tour = 0
    for tour in journey:
        if type(tour) == str:
            adjacent_bus_tour = 0
            total_cost += 2.4
        else:
            adjacent_bus_tour += 1
            if adjacent_bus_tour == 2:
                adjacent_bus_tour = 0
            else:
                total_cost += 1.5
    return f'£{total_cost:.2f}'
