def how_much_water(standard_water_requirement, maximum_items, items):
    if items < maximum_items:
        return 'Not enough clothes'
    if items > maximum_items * 2:
        return 'Too much clothes'
    return round(standard_water_requirement * 1.1 ** (items - maximum_items), 2)
