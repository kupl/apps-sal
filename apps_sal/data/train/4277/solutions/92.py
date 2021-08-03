def difference_in_ages(ages):
    ageDif = []
    ageDif.extend([min(ages), max(ages), max(ages) - min(ages)])
    return tuple(ageDif)
