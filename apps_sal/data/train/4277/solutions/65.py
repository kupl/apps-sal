def difference_in_ages(ages):
    bruh = list()
    bruh.append(min(ages))
    bruh.append(max(ages))
    bruh.append(max(ages) - min(ages))
    return tuple(bruh)
