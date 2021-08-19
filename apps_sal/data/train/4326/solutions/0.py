def london_city_hacker(journey):
    tube = 2.4
    bus = 1.5
    total_cost = 0.0
    count = 0
    for link in journey:
        if isinstance(link, str):
            total_cost += tube
            count = 0
        elif count == 0:
            total_cost += bus
            count += 1
        else:
            count = 0
    return '£{:.2f}'.format(total_cost)
